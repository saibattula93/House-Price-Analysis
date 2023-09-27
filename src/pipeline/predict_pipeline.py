import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path='C:\House_price\artifacts\model.pkl'
            preprocessor_path='artifacts\preprocessor.pkl'
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)



class CustomData:
    def __init__(  self,
        spend: int,
        permits: int,
        permit_val: float,
        starts: int,
        completions: int,
        manufactured: int,
        new_for_sale: int,
        months_supply: float,
        emratio: float,
        pop_level: int,
        gdp: float,
        mortgage_rate: float,
        fed_fund_rate: float,
        disp_income: float,
        pm_save: float,
        consump_durable: float,
        new_sold: int,
        rent_vacancy: float,
        owner_vacancy: float,
        week_earning: float,
        delinquent_rate: float,
        hor:float,
        hp_idx_qtr: float):

        self.spend = spend

        self.permits = permits

        self.permit_val = permit_val

        self.starts = starts

        self.completions = completions

        self.manufactured = manufactured

        self.new_for_sale = new_for_sale

        self.months_supply = months_supply

        self.emratio = emratio

        self.pop_level = pop_level

        self.gdp = gdp

        self.mortgage_rate = mortgage_rate

        self.fed_fund_rate = fed_fund_rate

        self.disp_income = disp_income

        self.pm_save = pm_save

        self.consump_durable = consump_durable

        self.new_sold = new_sold

        self.rent_vacancy = rent_vacancy

        self.owner_vacancy = owner_vacancy

        self.week_earning = week_earning

        self.delinquent_rate = delinquent_rate

        self.hor = hor

        self.hp_idx_qtr = hp_idx_qtr

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                                "spend" : [self.spend],
                               "permits" : [self.permits],
                                "permit_val" : [self.permit_val],
                                "starts" : [self.starts],
                                "completions" : [self.completions],
                                "manufactured" : [self.manufactured],
                                "new_for_sale" : [self.new_for_sale],
                                "months_supply" : [self.months_supply],
                                "emratio" : [self.emratio],
                                "pop_level" : [self.pop_level],
                                "gdp" : [self.gdp],
                                "mortgage_rate" : [self.mortgage_rate],
                                "fed_fund_rate" : [self.fed_fund_rate],
                                "disp_income" : [self.disp_income],
                                "pm_save" : [self.pm_save],
                                "consump_durable" : [self.consump_durable],
                                "new_sold" : [self.new_sold],
                                "rent_vacancy" : [self.rent_vacancy],
                                "owner_vacancy" : [self.owner_vacancy],
                                "week_earning" : [self.week_earning],
                                "delinquent_rate" : [self.delinquent_rate],
                                "hor" : [self.hor],
                                "hp_idx_qtr" : [self.hp_idx_qtr]
                                
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)