from sqlalchemy import create_engine, Engine

def get_engine(drivername:str, 
               host:str,
               user:str,
               password:str,
               port:int,
               database:str) -> Engine:
    
    url = get_connection_url(drivername, host, user, password, port, database)

    print(f'{url=}')

    engine = create_engine(url)

    return engine
    
def get_connection_url(drivername:str, 
                       host:str, 
                        user:str, 
                        password:str,
                        port:int,
                        database:str) -> str:
    

    url = f"{drivername}://{user}:{password}@{host}:{port}/{database}"

    return url