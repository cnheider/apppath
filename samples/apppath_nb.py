# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# Christian Heider Nielsen
# Created on 05/04/2020

# %%
from apppath import AppPath



# %%
apppath = AppPath("AppPath")
print(apppath.user_config)
print(apppath.user_log)
print(apppath.user_data)
print(apppath.user_cache)


