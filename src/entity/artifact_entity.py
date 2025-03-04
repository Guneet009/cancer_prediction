from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    train_file_path:str
    test_file_path:str

@dataclass
class DataValidationArtifact:
    valid_train_file_path:str
    valid_test_file_path:str
    invalid_train_file_path:str
    invalid_test_file_path:str
    drift_report_file_path:str

@dataclass
class DataTransformationArtifact:
    transformed_train_file_path:str
    transformed_test_file_path:str
    preprocessor_object_path:str

@dataclass
class ModelTrainerMetric:
    f1_score:float
    precision_score:float
    recall_score:float

@dataclass
class ModelTrainerArtifact:
    model_object_path:str
    training_data_artifact:ModelTrainerMetric
    test_data_artifact:ModelTrainerMetric
    