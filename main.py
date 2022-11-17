import requests

# Deploy public IP address
url = "https://management.azure.com/subscriptions/5b616edb-15b3-4b83-8096-e1195d43e088/resourceGroups/CloudComputing3rdYear_group/providers/Microsoft.Network/publicIPAddresses/cloudComputing?api-version=2022-05-01"

headers = {"Content-type": "application/json"}

data = {
    "properties": {
        "publicIPAllocationMethod": "Static",
        "idleTimeoutInMinutes": 10,
        "publicIPAddressVersion": "IPv4"
    },
    "sku": {
        "name": "Basic"
    },
    "location": "westeurope"
}

response = requests.put(url, headers=headers, json=data)

print("Status Code", response.status_code)
print("JSON Response ", response.json())

# Deploy Network interface card
url = "https://management.azure.com/subscriptions/5b616edb-15b3-4b83-8096-e1195d43e088/resourceGroups/CloudComputing3rdYear_group/providers/Microsoft.Network/networkInterfaces/networkInterface1?api-version=2022-05-01"

headers = {"Content-type": "application/json",
           "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IjJaUXBKM1VwYmpBWVhZR2FYRUpsOGxWMFRPSSIsImtpZCI6IjJaUXBKM1VwYmpBWVhZR2FYRUpsOGxWMFRPSSJ9.eyJhdWQiOiJodHRwczovL21hbmFnZW1lbnQuY29yZS53aW5kb3dzLm5ldCIsImlzcyI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0Lzc2NjMxN2NiLWU5NDgtNGU1Zi04Y2VjLWRhYmM4ZTJmZDVkYS8iLCJpYXQiOjE2Njg2OTc1OTMsIm5iZiI6MTY2ODY5NzU5MywiZXhwIjoxNjY4NzAzMjM1LCJhY3IiOiIxIiwiYWlvIjoiQVZRQXEvOFRBQUFBY2ZFV0hXVEdpNmg1THdiTG1YWUhycCs5VTZQQzFVcWh2UXhNaWNLSW56ZDBubmMyamwwWFo5dzR5RmMyVlAxbVZ5N2lFMVgrczJlZXNwWEFSSCtXUE5JNC9vdGpkbHBiZVQxNU0zOWdXWjg9IiwiYW1yIjpbInB3ZCIsIm1mYSJdLCJhcHBpZCI6IjE4ZmJjYTE2LTIyMjQtNDVmNi04NWIwLWY3YmYyYjM5YjNmMyIsImFwcGlkYWNyIjoiMCIsImZhbWlseV9uYW1lIjoiVGFiYW5pYWciLCJnaXZlbl9uYW1lIjoiRWlyYSIsImdyb3VwcyI6WyI4N2Y2MDAzZC05NDcwLTQzOGYtYmZlZi04MTNiMzdmYzJiNjgiLCJkMmE2YThlZi00ZDI2LTRkOTUtYmQxMS1hYTFlYzYxOWY4MTgiLCI5N2FmODEyZC05NmU5LTRmMDEtOGExMS03NTgwMzM3NjIxN2EiLCI4YzgxODZlYS00MmE0LTQ0YWYtOGE3OC1hZTkxNDAxMWU2YjQiLCI1YWQ3ZDZiNC1hZGFmLTRiOWQtOTU3Zi0wZjNiNjE0YmVlNjAiLCIxMjVjYWI3Yy1mOWViLTQzZTUtOWUyMS01ZTNiNWRkZDA1YmEiLCI4YWMxNTRkZC1kNDVmLTRjNDYtOTRlNS1iYjc4ZmVmYTNhZWYiXSwiaXBhZGRyIjoiMTQ3LjI1Mi4yMi4xMjMiLCJuYW1lIjoiQzIwNDYxMjg2IEVpcmEgVGFiYW5pYWciLCJvaWQiOiIxZWQ1NmZiMy1iM2I3LTQxNjMtYWI1ZC1lMThjNmQ5NjcwYTYiLCJvbnByZW1fc2lkIjoiUy0xLTUtMjEtMjAyNTQyOTI2NS0xOTU4MzY3NDc2LTcyNTM0NTU0My0zMjQ1MzgiLCJwdWlkIjoiMTAwMzIwMDBFNEFFMzU2MyIsInJoIjoiMC5BVEVBeXhkamRranBYMDZNN05xOGppX1Yya1pJZjNrQXV0ZFB1a1Bhd2ZqMk1CTXhBRVkuIiwic2NwIjoidXNlcl9pbXBlcnNvbmF0aW9uIiwic3ViIjoiNFRzVjdBUjl3VDUzdGQ1VS0zMXE3QXhBSE1ZTGpNMEdUYlBSTGJpbkM0RSIsInRpZCI6Ijc2NjMxN2NiLWU5NDgtNGU1Zi04Y2VjLWRhYmM4ZTJmZDVkYSIsInVuaXF1ZV9uYW1lIjoiQzIwNDYxMjg2QG15dHVkdWJsaW4uaWUiLCJ1cG4iOiJDMjA0NjEyODZAbXl0dWR1Ymxpbi5pZSIsInV0aSI6Im9JU0JWMDkyRVUtLUVyc3ZmYTBXQUEiLCJ2ZXIiOiIxLjAiLCJ3aWRzIjpbImI3OWZiZjRkLTNlZjktNDY4OS04MTQzLTc2YjE5NGU4NTUwOSJdLCJ4bXNfdGNkdCI6MTUyNTMzODk0MX0.SsbOhkSDW704msNnN-_KZNyuKKWq-0M0VJKgzTUg0sADJv0IU3KJ9SC4xSJD4Gi6R4_GpEBU7jxfpjGdfX8FIQKTDsmlluuL589XiaBizkbgr-VIELVmXOQ1OHIy03k7_KCRoDzfLh4oYFjWRu1YR7a8x187YOPr7C7ziZNge79eTAkEDmwXLq81bPwhiVgfDQG-t5FVb-ngOcDOdTy7nYLSQuszlraPdvkdZTE_py9GTGUu6_Zr2owdiYCMoFauOPr5A0AR1fuXR3ladzuq0hdRwgYmLmyI9MZGPOZSTPmsf4QR_-423C4UE8xqlluiF-8XOPA8T8IPH_x2fNIY9g"}

data = {
    "properties": {
    "ipConfigurations": [
    {
        "name": "ipconfig1",
        "properties": {
            "publicIPAddress": {
            "id": "/subscriptions/5b616edb-15b3-4b83-8096-e1195d43e088/resourceGroups/CloudComputing3rdYear_group/providers/Microsoft.Network/publicIPAddresses/cloudComputing"
        },
        "subnet": {
            "id": "/subscriptions/5b616edb-15b3-4b83-8096-e1195d43e088/resourceGroups/CloudComputing3rdYear_group/providers/Microsoft.Network/virtualNetworks/CloudComputing3rdYear_group-vnet/subnets/default"
            }
        }
    }
    ]
    },
    "location": "westeurope"
}
response = requests.put(url, headers=headers, json=data)

print("Status Code", response.status_code)
print("JSON Response ", response.json())

# Deploy Virtual Machine
url = "https://management.azure.com/subscriptions/5b616edb-15b3-4b83-8096-e1195d43e088/resourceGroups/CloudComputing3rdYear_group/providers/Microsoft.Compute/virtualMachines/CloudComputing3rdYearNew?api-version=2022-08-01"

headers = {"Content-type": "application/json",
           "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IjJaUXBKM1VwYmpBWVhZR2FYRUpsOGxWMFRPSSIsImtpZCI6IjJaUXBKM1VwYmpBWVhZR2FYRUpsOGxWMFRPSSJ9.eyJhdWQiOiJodHRwczovL21hbmFnZW1lbnQuY29yZS53aW5kb3dzLm5ldCIsImlzcyI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0Lzc2NjMxN2NiLWU5NDgtNGU1Zi04Y2VjLWRhYmM4ZTJmZDVkYS8iLCJpYXQiOjE2Njg2OTg4NTcsIm5iZiI6MTY2ODY5ODg1NywiZXhwIjoxNjY4NzA0MjMyLCJhY3IiOiIxIiwiYWlvIjoiQVZRQXEvOFRBQUFBVXZuK3EyMWtmWDlSMjZXR0JYejVaczdaTFZEOVo0bVlhYzhyYmRJV0pkY0RueEhjN2V4WjBUUGJnYXNrc05mSEFPeDBKYlp5dFQyRmNjRnY3WU80TVhmS3VxdmlNZEhkblltaTRsNS96MUk9IiwiYW1yIjpbInB3ZCIsIm1mYSJdLCJhcHBpZCI6IjE4ZmJjYTE2LTIyMjQtNDVmNi04NWIwLWY3YmYyYjM5YjNmMyIsImFwcGlkYWNyIjoiMCIsImZhbWlseV9uYW1lIjoiVGFiYW5pYWciLCJnaXZlbl9uYW1lIjoiRWlyYSIsImdyb3VwcyI6WyI4N2Y2MDAzZC05NDcwLTQzOGYtYmZlZi04MTNiMzdmYzJiNjgiLCJkMmE2YThlZi00ZDI2LTRkOTUtYmQxMS1hYTFlYzYxOWY4MTgiLCI5N2FmODEyZC05NmU5LTRmMDEtOGExMS03NTgwMzM3NjIxN2EiLCI4YzgxODZlYS00MmE0LTQ0YWYtOGE3OC1hZTkxNDAxMWU2YjQiLCI1YWQ3ZDZiNC1hZGFmLTRiOWQtOTU3Zi0wZjNiNjE0YmVlNjAiLCIxMjVjYWI3Yy1mOWViLTQzZTUtOWUyMS01ZTNiNWRkZDA1YmEiLCI4YWMxNTRkZC1kNDVmLTRjNDYtOTRlNS1iYjc4ZmVmYTNhZWYiXSwiaXBhZGRyIjoiMTQ3LjI1Mi4yMi4xMjMiLCJuYW1lIjoiQzIwNDYxMjg2IEVpcmEgVGFiYW5pYWciLCJvaWQiOiIxZWQ1NmZiMy1iM2I3LTQxNjMtYWI1ZC1lMThjNmQ5NjcwYTYiLCJvbnByZW1fc2lkIjoiUy0xLTUtMjEtMjAyNTQyOTI2NS0xOTU4MzY3NDc2LTcyNTM0NTU0My0zMjQ1MzgiLCJwdWlkIjoiMTAwMzIwMDBFNEFFMzU2MyIsInJoIjoiMC5BVEVBeXhkamRranBYMDZNN05xOGppX1Yya1pJZjNrQXV0ZFB1a1Bhd2ZqMk1CTXhBRVkuIiwic2NwIjoidXNlcl9pbXBlcnNvbmF0aW9uIiwic3ViIjoiNFRzVjdBUjl3VDUzdGQ1VS0zMXE3QXhBSE1ZTGpNMEdUYlBSTGJpbkM0RSIsInRpZCI6Ijc2NjMxN2NiLWU5NDgtNGU1Zi04Y2VjLWRhYmM4ZTJmZDVkYSIsInVuaXF1ZV9uYW1lIjoiQzIwNDYxMjg2QG15dHVkdWJsaW4uaWUiLCJ1cG4iOiJDMjA0NjEyODZAbXl0dWR1Ymxpbi5pZSIsInV0aSI6IlNjZ2pSYmQyQ2tHQWNreDE5RWNRQUEiLCJ2ZXIiOiIxLjAiLCJ3aWRzIjpbImI3OWZiZjRkLTNlZjktNDY4OS04MTQzLTc2YjE5NGU4NTUwOSJdLCJ4bXNfdGNkdCI6MTUyNTMzODk0MX0.C3_J8jiC3kjHoUw8o44i1SEVQ1qNGv3qvKhXivU5z31V2b_XdYeTyMxgAUBQBxhni4nWZmK0ptybEnLMzs4ltx5mi93d9J7P8ainhNOeV2Lc298IkTQZloKLqLsTJoPTXKiWG83w3g5j8E6aAxMcg4ErkYr5KTvQWkJt-dDN8hK_2dINL5ClVZQLL7WRFpi2d6y585SY-GzM-4Q3nMbUQMCboKLAe2LXj67ndS1j4D35NFZXKGyH_451mIwgLNtPw-KA0Ne4OrL8ZQF-OYf_7b_kl4vkDj9-9vrFQS5zBOj6MHUrub8ZdAE-eldEAqw4i86wy0WB1GqEzaXAWkMMtA"}

data = {
"id": "/subscriptions/5b616edb-15b3-4b83-8096-e1195d43e088/resourceGroups/CloudComputing3rdYear_group/providers/Microsoft.Compute/virtualMachines/CloudComputing3rdYearNew",
"type": "Microsoft.Compute/virtualMachines",
"properties": {
"osProfile": {
"adminUsername": "enjoy",
"secrets": [
],
"computerName": "CloudComputing3rdYearNew",
"linuxConfiguration": {
"ssh": {
"publicKeys": [
{
"path": "/home/enjoy/.ssh/authorized_keys",
"keyData": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCxgeJo0sXCaumlA1nQAkTXi1m9ZtsbuvDyMutOACDN/rj2wP0uxsJPA98TFcj8XvTG1mpzy93RbU40RHUq0xisuM5daBUiyld2nPKKghGDYTbBUFuYRmHb8X5fLRsFBWrMNjhwJxD0n2ZuUTS5yqFG+A/AvH6XX8rh6q9LgctmXInECuvKYwmSr2p5dvWF7rxhGMQMpjGXsBK5hkP+ddcTLPjnEMdkSqpqKqIZFqF7gA87A+OK9b7C5Wwv1ZwIMnVPLvQU8D7K6utfQGixsTNqy6thZkKCkbO9cavEk6WcR5PBeNizm5jP6vTNLjmrbMqqxksGHAnmQCUnnO6gZc//R1WymsrkpR4dbb9f0bSKOQQ9MhyiYBDHdN/VWewxN9rFVaTH9rXOz+HAaeAM4Rua3iRLgyHzrgkw6fmjiulSuoUVUBGJEn6OKjqJKvToOxJh4+NgEFChhHCsXytzE9TUvS8fHD2y4W+0QugflkITSinPpdRNEJR+vFrlXmfg3q8= enjoy@enjoy-HP-Pavilion-Notebook"
}
]
},
"disablePasswordAuthentication": True
}
},
"networkProfile": {
"networkInterfaces": [
{
"id": "/subscriptions/5b616edb-15b3-4b83-8096-e1195d43e088/resourceGroups/CloudComputing3rdYear_group/providers/Microsoft.Network/networkInterfaces/networkInterface1",
"properties": {
"primary": True
}
}
]
},
"storageProfile": {
"imageReference": {
"sku": "16.04-LTS",
"publisher": "Canonical",
"version": "latest",
"offer": "UbuntuServer"
},
"dataDisks": [
]
},
"hardwareProfile": {
"vmSize": "Standard_D1_v2"
},
"provisioningState": "Creating"
},
"name": "CloudComputing3rdYearNew",
"location": "westeurope"
}

response = requests.put(url, headers=headers, json=data)

print("Status Code", response.status_code)
print("JSON Response ", response.json())
