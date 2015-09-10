'''
Created on 2015. 9. 4.

@author: Jay
'''

class IndicatorType():
    
    class IndicatorType_MA(enumerate):
        SimpleMovingAverage5Day = "SimpleMovingAverage5Day"
        SimpleMovingAverage20Day = "SimpleMovingAverage20Day"
        SimpleMovingAverage60Day = "SimpleMovingAverage60Day"
        SimpleMovingAverage120Day = "SimpleMovingAverage120Day"
        WeightedMovingAverage5Day = "WeightedMovingAverage5Day"
        WeightedMovingAverage20Day = "WeightedMovingAverage20Day"
        WeightedMovingAverage60Day = "WeightedMovingAverage60Day"
        WeightedMovingAverage120Day = "WeightedMovingAverage120Day"
        ExponentialWeightedMovingAverage5Day = "ExponentialWeightedMovingAverage5Day"
        ExponentialWeightedMovingAverage20Day = "ExponentialWeightedMovingAverage20Day"
        ExponentialWeightedMovingAverage60Day = "ExponentialWeightedMovingAverage60Day"
        ExponentialWeightedMovingAverage120Day = "ExponentialWeightedMovingAverage120Day"
        
        list = [
            SimpleMovingAverage5Day, SimpleMovingAverage20Day, 
            SimpleMovingAverage60Day, SimpleMovingAverage120Day, 
            WeightedMovingAverage5Day, WeightedMovingAverage20Day,
            WeightedMovingAverage60Day, WeightedMovingAverage120Day,
            ExponentialWeightedMovingAverage5Day, ExponentialWeightedMovingAverage20Day,
            ExponentialWeightedMovingAverage60Day, ExponentialWeightedMovingAverage120Day
        ]
        
    class IndicatorType_AD(enumerate):
        AccumulationDistricutionIndex= "AccumulationDistricutionIndex"
        
        list = [
            AccumulationDistricutionIndex,
        ]
    
    class IndicatorType_Volatility(enumerate):
        Volatility5Day = "Volatility5Day"
        Volatility20Day = "Volatility20Day"
        list = [
            Volatility5Day, Volatility20Day,
        ]

    dataTableMap = {
        IndicatorType_MA.SimpleMovingAverage5Day : "MASi005",
        IndicatorType_MA.SimpleMovingAverage20Day : "MASi020",
        IndicatorType_MA.SimpleMovingAverage60Day : "MASi060",
        IndicatorType_MA.SimpleMovingAverage120Day : "MASi120",
        IndicatorType_MA.WeightedMovingAverage5Day : "MAW005",
        IndicatorType_MA.WeightedMovingAverage20Day : "MAW020",
        IndicatorType_MA.WeightedMovingAverage60Day : "MAW060",
        IndicatorType_MA.WeightedMovingAverage120Day : "MAW120",
        IndicatorType_MA.ExponentialWeightedMovingAverage5Day : "MAEW005",
        IndicatorType_MA.ExponentialWeightedMovingAverage20Day : "MAEW020",
        IndicatorType_MA.ExponentialWeightedMovingAverage60Day : "MAEW060",
        IndicatorType_MA.ExponentialWeightedMovingAverage120Day : "MAEW120",
        IndicatorType_AD.AccumulationDistricutionIndex : "AD000",
        IndicatorType_Volatility.Volatility5Day : "VOL005",
        IndicatorType_Volatility.Volatility20Day : "VOL020",
    }
    
    
    
    