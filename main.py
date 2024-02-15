# main.py

from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from fastapi.responses import JSONResponse
import mysql.connector

app = FastAPI()

def connect():
    return mysql.connector.connect(
        host='127.0.0.1',
        user='manish',
        password='manish12',
        database='football',
        auth_plugin='mysql_native_password'  
    )

origins = [
    "http://127.0.0.1",
    "http://127.0.0.1:8000",
    "http://127.0.0.1:5500",
]
# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Update with your actual frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# @app.get("/")      #The @app.get("/") tells FastAPI that the function right below is in charge of handling requests that go to the path / using a get operation. 
# async def root():  #This function will be called by FastAPI whenever it receives a request to the specified URL (/) using a GET operation.
#     return {"message": "Hello World"}

class Player(BaseModel):
    PlayerId:int
    PlayerName:str
    Position: str
    TeamId:int
    MatchesPlayed: int
    Starts:int
    MinutesPlayed:int
    MinutesPlayedPer90:int
    Goals:int
    Assists:int
    SumGoalsAssists:int
    NonPenaltyGoals:int
    PenaltiesMade:int
    PenaltiesAttempted:int
    YellowCards:int
    RedCards: int
    ExpectedGoalsxG: float
    NonPenaltyGoalsnpxG:float
    ExpectedAssistedGoalsxAG:float
    npxGplusxAG:float
    ProgressiveCarries:int
    ProgressivePasses:int
    ProgressivepassesReceived:int
    Per90MinutesGoals:float
    Per90MinutesAssists:float
    Per90MinutesGplusA:float
    Per90MinutesNonPenaltyGoals:float
    Per90MinutesGplusAsubPK:float
    Per90MinutesxG:float
    Per90MinutesxAG:float
    Per90MinutesxGplusxAG:float
    Per90MinutesnpxG:float
    Per90MinutesnpxGplusxAG:float
    CountryCode: str
    PlayerAge:int 

class Team(BaseModel):
    TeamId: int
    TeamName: str
    CountryCode: str
    LeagueId:int
    ManagerId:int
    StadiumId:int
    LeagueRank:int
    MP: int
    W:int
    D:int
    L:int
    GF:int
    GA:int
    GD:int
    Pts:int
    PtsperMP:float
    xG:float
    xGA:float
    xGD:float
    xGDper90:float
    Attendance:int

class Country(BaseModel):
    CountyCode: str
    CountryName: str

class League(BaseModel):
    LeagueId: int
    LeagueName: str
    CountryCode:str

class Manager(BaseModel):
    ManagerId: int
    ManagerName:str
    CountryCode: str
    Age: int

class Stadium(BaseModel):
    StadiumId: int
    StadumName: str
    Location: str
    Capacity: int
    
    
@app.get("/players", response_model=List[Player])
async def read_players():
    try:
        #connect to database
        db = connect()

        # Perform database operations
        with db.cursor() as cursor:
            cursor.execute("SELECT * FROM players")
            players = cursor.fetchall()

        # Close the database connection
        db.close()

        # Return a JSON response with the fetched players
        return JSONResponse(content={"data": players})

    except Exception as e:
        # Handle exceptions, such as database connection errors
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

@app.get("/teams", response_model=List[Team])
async def read_teams():
    try:
        #connect to database
        db = connect()

        # Perform database operations
        with db.cursor() as cursor:
            cursor.execute("SELECT * FROM teams")
            teams = cursor.fetchall()

        # Close the database connection
        db.close()

        # Return a JSON response with the fetched players
        return JSONResponse(content={"data": teams})

    except Exception as e:
        # Handle exceptions, such as database connection errors
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    
@app.get("/countries", response_model=List[Country])
async def read_countries():
    try:
        #connect to database
        db = connect()

        # Perform database operations
        with db.cursor() as cursor:
            cursor.execute("SELECT * FROM countries")
            countries = cursor.fetchall()

        # Close the database connection
        db.close()

        # Return a JSON response with the fetched players
        return JSONResponse(content={"data": countries})

    except Exception as e:
        # Handle exceptions, such as database connection errors
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")


@app.get("/leagues", response_model=List[League])
async def read_leagues():
    try:
        #connect to database
        db = connect()

        # Perform database operations
        with db.cursor() as cursor:
            cursor.execute("SELECT * FROM leagues")
            leagues = cursor.fetchall()

        # Close the database connection
        db.close()

        # Return a JSON response with the fetched players
        return JSONResponse(content={"data": leagues})

    except Exception as e:
        # Handle exceptions, such as database connection errors
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    
@app.get("/manager", response_model=List[Manager])
async def read_manager():
    try:
        #connect to database
        db = connect()

        # Perform database operations
        with db.cursor() as cursor:
            cursor.execute("SELECT * FROM manager")
            manager = cursor.fetchall()

        # Close the database connection
        db.close()

        # Return a JSON response with the fetched players
        return JSONResponse(content={"data": manager})

    except Exception as e:
        # Handle exceptions, such as database connection errors
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    
@app.get("/stadium", response_model=List[Stadium])
async def read_teams():
    try:
        #connect to database
        db = connect()

        # Perform database operations
        with db.cursor() as cursor:
            cursor.execute("SELECT * FROM stadium")
            stadium = cursor.fetchall()

        # Close the database connection
        db.close()

        # Return a JSON response with the fetched players
        return JSONResponse(content={"data": stadium})

    except Exception as e:
        # Handle exceptions, such as database connection errors
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")


# sort player name by letter
def generate_sql_query_letters(letter):
    return f"SELECT * FROM players WHERE `PlayerName` LIKE '{letter}%';"

@app.get("/players/letters/{letter}", response_model=List[Player])
async def read_players_letters(letter: str):
    try:
        #connect to database
        db = connect()

        # Perform database operations
        with db.cursor() as cursor:
            query = generate_sql_query_letters(letter)
            cursor.execute(query)
            players = cursor.fetchall()

        # Close the database connection
        db.close()

        # Return a JSON response with the fetched players
        return JSONResponse(content={"data": players})

    except Exception as e:
        # Handle exceptions, such as database connection errors
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

# Search player by nationality
def generate_sql_query_nationality(CountryName):
    return f"SELECT PlayerId,PlayerName,Position FROM players AS p INNER JOIN countries  AS c ON c.`CountryCode`=p.`CountryCode`WHERE c.`CountryName`='{CountryName}';"

@app.get("/players/nationality/{CountryName}", response_model=List[Player])
async def read_players_nationality(CountryName: str):
    try:
        #connect to database
        db = connect()

        # Perform database operations
        with db.cursor() as cursor:
            query = generate_sql_query_nationality(CountryName)
            cursor.execute(query)
            players = cursor.fetchall()

        # Close the database connection
        db.close()

        # Return a JSON response with the fetched players
        return JSONResponse(content={"data": players})

    except Exception as e:
        # Handle exceptions, such as database connection errors
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")



# Search player by Clubs
def generate_sql_query_clubs(TeamName):
    return f"SELECT PlayerName FROM players AS p INNER JOIN teams AS t ON t.`TeamId`=p.`TeamId` WHERE t.`TeamName`='{TeamName}';"

@app.get("/players/club/{TeamName}", response_model=List[Player])
async def read_players_clubs(TeamName: str):
    try:
        #connect to database
        db = connect()

        # Perform database operations
        with db.cursor() as cursor:
            query = generate_sql_query_clubs(TeamName)
            cursor.execute(query)
            players = cursor.fetchall()

        # Close the database connection
        db.close()

        # Return a JSON response with the fetched players
        return JSONResponse(content={"data": players})

    except Exception as e:
        # Handle exceptions, such as database connection errors
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    


# Search player by LeagueName
def generate_sql_query_leaguename(LeagueName):
    return f"SELECT PlayerName FROM players AS p INNER JOIN teams as t ON p.`TeamId`=t.`TeamId` INNER JOIN leagues AS l ON t.`LeagueId`=l.`LeagueId` WHERE l.`LeagueName`='{LeagueName}';"


@app.get("/players/leagueName/{LeagueName}", response_model=List[Player])
async def read_players_leaguename(LeagueName: str):
    try:
        #connect to database
        db = connect()

        # Perform database operations
        with db.cursor() as cursor:
            query = generate_sql_query_leaguename(LeagueName)
            cursor.execute(query)
            players = cursor.fetchall()

        # Close the database connection
        db.close()

        # Return a JSON response with the fetched players
        return JSONResponse(content={"data": players})

    except Exception as e:
        # Handle exceptions, such as database connection errors
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    
# PlayerComparison
def generate_sql_query_Comparison(player1,player2):
    return f"select * from players where PlayerName in (Select PlayerName from players where PlayerName = '{player1}' OR PlayerName = '{player2}') ;"


@app.get("/players/Comparison/{player1}/{player2}", response_model=List[Player])
async def read_players_Comparison(player1: str,player2:str):
    try:
        #connect to database
        db = connect()

        # Perform database operations
        with db.cursor() as cursor:
            query = generate_sql_query_Comparison(player1,player2)
            cursor.execute(query)
            players = cursor.fetchall()

        # Close the database connection
        db.close()

        return JSONResponse(content={"data": players})

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")


# stats of particular player  
def generate_sql_query_particular_player(player1):
    return f"select * from players where PlayerName='{player1}';"

@app.get("/players/playerstats/{player}", response_model=List[Player])
async def read_players_particular_player(player1: str):
    try:
        #connect to database
        db = connect()

        # Perform database operations
        with db.cursor() as cursor:
            query = generate_sql_query_particular_player(player1)
            cursor.execute(query)
            players = cursor.fetchall()

        # Close the database connection
        db.close()

        return JSONResponse(content={"data": players})

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
