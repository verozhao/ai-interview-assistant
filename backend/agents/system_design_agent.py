class SystemDesignAgent:
    def __init__(self):
        self.components = {
            "storage": ["SQL", "NoSQL", "ObjectStore", "VectorDB"],
            "compute": ["GPU", "TPU", "CPU cluster"],
            "serving": ["REST", "gRPC", "GraphQL", "WebSocket"],
            "ml_specific": ["Feature Store", "Model Registry", "A/B Testing"]
        }
    
    async def design_system(self, requirements: str) -> Dict:
        # Parse requirements
        scale = self.extract_scale(requirements)
        ml_needs = self.identify_ml_components(requirements)
        
        # Generate architecture
        architecture = {
            "data_pipeline": self.design_data_pipeline(scale),
            "training_infra": self.design_training_infra(ml_needs),
            "serving_layer": self.design_serving(scale),
            "monitoring": self.design_monitoring()
        }
        
        # Create visual diagram
        diagram = self.generate_architecture_diagram(architecture)
        
        return {
            "architecture": architecture,
            "diagram": diagram,
            "cost_estimate": self.estimate_cost(architecture, scale),
            "tradeoffs": self.analyze_tradeoffs(architecture)
        }