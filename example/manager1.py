#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 13:56:48 2019

@author: slo
"""

from regularflow import newAgent, cycleManager, startDemo, startAgent

consumerConfig = {
                'bootstrap.servers': 'localhost:9092',
                'group.id': 'manager',
                'auto.offset.reset': 'earliest'
                }
producerConfig = {
                'bootstrap.servers': 'localhost:9092'
                 }

agent = newAgent(1, consumerConfig, producerConfig, "cluster0", "manager0","display", "manager")
agent._setAgents([1])
cycleManager([agent], [-1])
startAgent(agent)
