#!/bin/bash

# Define la tabla de DynamoDB

# Lee los ítems desde el archivo JSON
items=$(cat datos.json)

# Inserta los elementos en la tabla usando batch-write-item
aws dynamodb batch-write-item \
  --request-items "$items"
