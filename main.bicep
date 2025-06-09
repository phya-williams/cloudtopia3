param location string = 'eastus'
param storageAccountName string = 'cloudtopiablob2025'
param containerName string = 'weatherdata'

resource storage 'Microsoft.Storage/storageAccounts@2022-09-01' = {
  name: storageAccountName
  location: location
  kind: 'StorageV2'
  sku: {
    name: 'Standard_LRS'
  }
  properties: {
    accessTier: 'Hot'
  }
}

resource container 'Microsoft.Storage/storageAccounts/blobServices/containers@2022-09-01' = {
  name: containerName
  properties: {
    publicAccess: 'None'
  }
}

resource staticWebsite 'Microsoft.Storage/storageAccounts/staticWebsite@2022-09-01' = {
  parent: storage
  name: 'default'
  properties: {
    indexDocument: 'index.html'
    error404Document: '404.html'
  }
}
