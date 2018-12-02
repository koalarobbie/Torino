#-*- coding: UTF-8 -*-
import tushare as ts

class Portfolio(object):
    '''

    '''
    def __init__(self, stocks, events, start_date, initial_capital=100000.00):
        self.stocks = stocks    #投资组合的股票列表，每只股票包括股票代码和数量
        self.events = events    #消息队列
        self.capital = initial_capital  #资金，按人民币计算
        self.start_date = start_date    #起始日期
        self.date = self.start_date     #当前日期

        