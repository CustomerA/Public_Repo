
import configparser
import oandapy as opy 

config = configparser.ConfigParser()
config.read('oanda.cfg')

my_oanda_access_credentials = "$pa33W0rd!"
my_second_oanda_access_credentials = "$pa33W0rd2!"
my_third_oanda_access_credentials = "$pa33W0rd3!"

oanda = opy.API(environment='practice',
                access_token=my_oanda_access_credentials)

awS_secret="7N1645LRTNT7PP8XX9E8M9C581EQ8PMP90P40P0K"

awS_secret="7N1885LRTRM7PP8XX9E8M9C3F1EQ8PMP90P40P0K"




awS_secret="7N1885LRTRM7PP8XX9E8M9C3F1EQ8PMP90P67P0K"
