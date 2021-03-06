#!/usr/bin/python

## @validator_request.py
#  This file validates user supplied GPS coordinates (longitude, latitude), and
#      parameters (radius, days back).
from package.validator_functions import validate_longitude, validate_latitude, validate_radius, validate_daysBack, validate_dataset_url

## validate_request: validate received request parameters.
def validate_request( origin ):
  list_error = []

  # validation logic
  validated_longitude   = validate_longitude( origin['longitude'] )
  validated_latitude    = validate_latitude( origin['latitude'] )
  validated_dataset_url = validate_dataset_url( origin['dataset'] )
  validated_radius      = validate_radius( origin['radius'] )
  validated_daysBack    = validate_daysBack( origin['daysBack'] )

  # append error(s)
  if not validated_longitude['status']: list_error.append( validated_longitude['error'] )
  if not validated_latitude['status']: list_error.append( validated_latitude['error'] )
  if not validated_dataset_url['status']: list_error.append( validated_dataset_url['error'] )
  if not validated_radius['status']: list_error.append( validated_radius['error'] )
  if not validated_daysBack['status']: list_error.append( validated_daysBack['error'] )

  # return error(s)
  if len(list_error) > 0:
    return { 'status': False, 'error': list_error }
  else:
    return { 'status': True, 'error': None }
