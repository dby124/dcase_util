import dcase_util
chain = dcase_util.processors.ProcessingChain([
    {
        'processor_name': 'dcase_util.processors.MonoAudioReadingProcessor',
        'init_parameters': {
            'fs': 44100
        }
    },
    {
        'processor_name': 'dcase_util.processors.RepositoryFeatureExtractorProcessor',
        'init_parameters': {
            'parameters': {
                'mel': {},
                'mfcc': {}
            }
        }
    },
    {
        'processor_name': 'dcase_util.processors.StackingProcessor',
        'init_parameters': {
            'recipe': 'mel;mfcc=1-19'
        }
    }
])
# Run the processing chain
data = chain.process(filename=dcase_util.utils.Example().audio_filename())
data.plot()