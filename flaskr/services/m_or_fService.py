from flaskr.models.m_or_f import MorF

class MoFService:

    def get_list(self) -> list:
        return  MorF.query.all()