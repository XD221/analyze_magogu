import redis
import pandas as p
import numpy as np
import streamlit as st
from glob import glob

# * Connection db
redis_con = redis.Redis(
    host='redis_7.0.5',
    port=6379,
    password='1234'
)