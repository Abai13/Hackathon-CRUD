class Settings:
    
    TOKEN: dict = {'Authorization': 'Bearer keyeMyDjXvb7qDruk',"Content-Type": "application/json" }
    TOKEN_UNI = 'Bearer keyeMyDjXvb7qDruk'
    TABLE_NAME: str = 'Cars' 
    BASE_ID: str = 'appBIIgBUC1fkOEgB' 

    LIST_RECORDS_URL: str = f'?maxRecords=3&view=Grid%20view'
    CREATE_RECORD_URL: str = f'/{BASE_ID}/{TABLE_NAME}'


    @property
    def get_url(self):
        return f'https://api.airtable.com/v0/{self.BASE_ID}/{self.TABLE_NAME}'


settings = Settings()
