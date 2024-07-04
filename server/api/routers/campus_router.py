from fastapi import APIRouter, Response, status, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import uuid4

# from database import get_db
from schemas.campus import CampusSchema
from models.campus_model import Campus as CampusModel

def get_db():
    pass

router = APIRouter()

@router.post('', status_code=status.HTTP_201_CREATED)
def create_campus(campus: CampusSchema, db:Session = Depends(get_db)):

    try:

        new_campus = CampusModel(name=campus.name, 
                                 code=campus.code,
                                 )
        
        db.add(new_campus)
        db.commit()

        return new_campus.to_dict()
    
    except Exception as err:

        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

@router.get('')
async def get_campus(db:Session=Depends(get_db)):

    return db.query(CampusModel).filter(CampusModel.active).all()


@router.get('/{campus_id}', status_code=status.HTTP_200_OK)
def get_campus_by_id(campus_id: str, db:Session = Depends(get_db)):


    campus = db.query(CampusModel).filter(CampusModel.campus_id == campus_id).filter(CampusModel.active).first()

    if not campus:

        return Response(status_code=status.HTTP_404_NOT_FOUND)
    
    return campus

@router.put('/{campus_id}', status_code=status.HTTP_200_OK)
def delete_Campus(campus_id: str, campus: CampusSchema, db:Session = Depends(get_db)):

    db_campus = db.query(CampusModel).filter(CampusModel.campus_id == campus_id).filter(CampusModel.active).first()

    if not db_campus:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    
    db_campus.name = campus.name
    db_campus.code = campus.code

    db.commit()
    db.refresh(db_campus)

    return db_campus.to_dict()


@router.delete('/{campus_id}', status_code=status.HTTP_200_OK)
def delete_Campus(campus_id: str, db:Session = Depends(get_db)):

    campus = db.query(CampusModel).filter(CampusModel.campus_id == campus_id).filter(CampusModel.active).first()

    if not campus:

        return Response(status_code=status.HTTP_404_NOT_FOUND)
    
    campus.delete()

    db.commit()
    db.refresh(campus)

    return campus.to_dict()


