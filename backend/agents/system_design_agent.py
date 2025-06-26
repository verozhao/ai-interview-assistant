class SystemDesignAgent(BaseAgent):
    def __init__(self):
        super().__init__()
        self.components = {
            "data_layer": ["PostgreSQL", "MongoDB", "Cassandra", "Redis"],
            "compute": ["EC2", "Kubernetes", "Lambda", "Fargate"],
            "ml_serving": ["SageMaker", "TorchServe", "TF Serving", "Triton"],
            "streaming": ["Kafka", "Kinesis", "Pub/Sub", "EventHub"],
            "monitoring": ["Prometheus", "DataDog", "CloudWatch", "Grafana"]
        }
    
    async def process(self, question: str, context: Dict[str, Any]) -> Dict:
        # Extract requirements
        requirements = await self.extract_requirements(question)
        
        # Design architecture
        architecture = await self.design_system(requirements)
        
        # Add ML-specific components
        if "ml" in question.lower() or "ai" in question.lower():
            architecture["ml_pipeline"] = self.design_ml_pipeline(requirements)
        
        # Generate diagrams
        diagram_code = self.generate_diagram(architecture)
        
        return {
            "requirements": requirements,
            "architecture": architecture,
            "diagram": diagram_code,
            "tradeoffs": self.analyze_tradeoffs(architecture),
            "scaling": self.design_scaling_strategy(requirements),
            "cost_estimate": self.estimate_cost(architecture)
        }