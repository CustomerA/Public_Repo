
import configparser
import oandapy as opy 

config = configparser.ConfigParser()
config.read('oanda.cfg')

my_oanda_access_credentials = "$pa33W0rd!"
my_second_oanda_access_credentials = "$pa33W0rd2!"
my_third_oanda_access_credentials = "$pa33W0rd3!"

oanda = opy.API(environment='practice',
                access_token=my_oanda_access_credentials)

`sk_test_MfRuaFA9sgl5e1BUYzjwiNNt00UM6t6fvY`

aWs_account: "3238-1074-5335”

Maurice
