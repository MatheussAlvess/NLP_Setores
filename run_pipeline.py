
from NLPPipeline import Pipeline 


# Altere os parametros como achar melhor
params = {
    'dataset_path': 'dataset/',
    'dataset_name': 'dataset.csv',
    'sentences_variable': 'sentence',
    'categories_variable': 'category',
    'model_name': 'cnn_model.keras',
    'save': True,
    'emb_dim': 128,
    'nb_filters': 100,
    'ffn_units': 512,
    'nb_classes': 5,
    'batch_size': 32,
    'dropout_rate': 0.2,
    'nb_epochs': 100,
    'verbose': 1}


# Executa pipeline 
pipeline = Pipeline(**params)
pipeline.processing_dataset()
pipeline.run_model()
pipeline.predict_sector('Curso de LIBRAS.')