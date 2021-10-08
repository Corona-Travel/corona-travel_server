import importlib.metadata

_DISTRIBUTION_METADATA = importlib.metadata.metadata("corona_travel_server")

__authors__ = _DISTRIBUTION_METADATA['Author']
__project__ = _DISTRIBUTION_METADATA['Name']
__version__ = _DISTRIBUTION_METADATA['Version']
