import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import pdfkit

st.set_page_config(page_title="Explore Weather Trends App",page_icon="⛅️")

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

city_list = {
    0: 'Abidjan', 1: 'Abu Dhabi', 2: 'Abuja', 3: 'Accra', 4: 'Adana', 5: 'Adelaide', 6: 'Agra', 7: 'Ahmadabad', 8: 'Albuquerque', 9: 'Alexandria', 10: 'Alexandria', 11: 'Algiers', 12: 'Allahabad', 13: 'Almaty', 14: 'Amritsar', 15: 'Amsterdam', 16: 'Ankara', 17: 'Anshan', 18: 'Antananarivo', 19: 'Arlington', 20: 'Asmara', 21: 'Astana', 22: 'Athens', 23: 'Atlanta', 24: 'Austin', 25: 'Baghdad', 26: 'Baku', 27: 'Baltimore', 28: 'Bamako', 29: 'Bandung', 30: 'Bangalore', 31: 'Bangkok', 32: 'Bangui', 33: 'Barcelona', 34: 'Barcelona', 35: 'Barquisimeto', 36: 'Barranquilla', 37: 'Beirut', 38: 'Belfast', 39: 'Belgrade', 40: 'Belo Horizonte', 41: 'Benghazi', 42: 'Berlin', 43: 'Bern', 44: 'Bhopal', 45: 'Birmingham', 46: 'Birmingham', 47: 'Bissau', 48: 'Boston', 49: 'Bratislava', 50: 'Brazzaville', 
    51: 'Brisbane', 52: 'Brussels', 53: 'Bucharest', 54: 'Budapest', 55: 'Bujumbura', 56: 'Bursa', 57: 'Cairo', 58: 'Cali', 59: 'Campinas', 60: 'Canberra', 61: 'Caracas', 62: 'Cardiff', 63: 'Casablanca', 64: 'Changchun', 65: 'Changzhou', 66: 'Charlotte', 67: 'Chelyabinsk', 68: 'Chengdu', 69: 'Chicago', 70: 'Chisinau', 71: 'Colombo', 72: 'Colombo', 73: 'Colorado Springs', 74: 'Columbus', 75: 'Conakry', 76: 'Copenhagen', 77: 'Cordoba', 78: 'Curitiba', 79: 'Dakar', 80: 'Dalian', 81: 'Dallas', 82: 'Damascus', 83: 'Dar Es Salaam', 84: 'Datong', 85: 'Delhi', 86: 'Denver', 87: 'Detroit', 88: 'Dhaka', 89: 'Doha', 90: 'Douala', 91: 'Dublin', 92: 'Durban', 93: 'Dushanbe', 94: 'Ecatepec', 95: 'Edinburgh', 96: 'El Paso', 97: 'Faisalabad', 98: 'Fort Worth', 99: 'Fortaleza', 100: 'Foshan', 
    101: 'Freetown', 102: 'Fresno', 103: 'Fuzhou', 104: 'Gaborone', 105: 'Georgetown', 106: 'Guadalajara', 107: 'Guangzhou', 108: 'Guarulhos', 109: 'Guatemala City', 110: 'Guayaquil', 111: 'Guiyang', 112: 'Gujranwala', 113: 'Hamburg', 114: 'Handan', 115: 'Hangzhou', 116: 'Hanoi', 117: 'Haora', 118: 'Harare', 119: 'Harbin', 120: 'Hefei', 121: 'Helsinki', 122: 'Hiroshima', 123: 'Ho Chi Minh City', 124: 'Houston', 125: 'Hyderabad', 126: 'Hyderabad', 127: 'Ibadan', 128: 'Indianapolis', 129: 'Indore', 130: 'Irbil', 131: 'Islamabad', 132: 'Istanbul', 133: 'Izmir', 134: 'Jacksonville', 135: 'Jaipur', 136: 'Jakarta', 137: 'Jilin', 138: 'Jinan', 139: 'Johannesburg', 140: 'Juba', 141: 'Kabul', 142: 'Kaduna', 143: 'Kampala', 144: 'Kano', 145: 'Kanpur', 146: 'Kansas City', 147: 'Karachi', 148: 'Kathmandu', 149: 'Kawasaki', 150: 'Kazan',
    151: 'Khartoum', 152: 'Khulna', 153: 'Kiev', 154: 'Kigali', 155: 'Kingston', 156: 'Kingston', 157: 'Kinshasa', 158: 'Kitakyushu', 159: 'Kobe', 160: 'Kuala Lumpur', 161: 'Kunming', 162: 'La Paz', 163: 'La Paz', 164: 'Lagos', 165: 'Lahore', 166: 'Lanzhou', 167: 'Las Vegas', 168: 'Libreville', 169: 'Lilongwe', 170: 'Lima', 171: 'Lisbon', 172: 'Ljubljana', 173: 'London', 174: 'London', 175: 'Long Beach', 176: 'Los Angeles', 177: 'Los Angeles', 178: 'Louisville', 179: 'Luanda', 180: 'Lubumbashi', 181: 'Ludhiana', 182: 'Luoyang', 183: 'Lusaka', 184: 'Madrid', 185: 'Maiduguri', 186: 'Malabo', 187: 'Managua', 188: 'Manama', 189: 'Manaus', 190: 'Manila', 191: 'Maputo', 192: 'Maracaibo', 193: 'Maseru', 194: 'Mashhad', 195: 'Mecca', 196: 'Medan', 197: 'Melbourne', 198: 'Memphis', 199: 'Mesa', 200: 'Mexicali', 
    201: 'Miami', 202: 'Milan', 203: 'Milwaukee', 204: 'Minneapolis', 205: 'Minsk', 206: 'Mogadishu', 207: 'Monrovia', 208: 'Monterrey', 209: 'Montevideo', 210: 'Montreal', 211: 'Moscow', 212: 'Multan', 213: 'Munich', 214: 'Nagoya', 215: 'Nagpur', 216: 'Nairobi', 217: 'Nanchang', 218: 'Nanjing', 219: 'Nanning', 220: 'Nashville', 221: 'Nassau', 222: 'New Delhi', 223: 'New Orleans', 224: 'New York', 225: 'Niamey', 226: 'Nouakchott', 227: 'Novosibirsk', 228: 'Oakland', 229: 'Oklahoma City', 230: 'Omaha', 231: 'Omsk', 232: 'Oslo', 233: 'Ottawa', 234: 'Ouagadougou', 235: 'Palembang', 236: 'Paramaribo', 237: 'Paris', 238: 'Patna', 239: 'Perm', 240: 'Perth', 241: 'Peshawar', 242: 'Philadelphia', 243: 'Phoenix', 244: 'Podgorica', 245: 'Port Au Prince', 246: 'Port Harcourt', 247: 'Port Louis', 248: 'Port Moresby', 249: 'Portland', 250: 'Porto Alegre', 
    251: 'Prague', 252: 'Pretoria', 253: 'Pristina', 254: 'Puebla', 255: 'Pune', 256: 'Qingdao', 257: 'Qiqihar', 258: 'Quito', 259: 'Rabat', 260: 'Rajkot', 261: 'Raleigh', 262: 'Ranchi', 263: 'Rawalpindi', 264: 'Recife', 265: 'Riga', 266: 'Rio De Janeiro', 267: 'Riyadh', 268: 'Rome', 269: 'Rosario', 270: 'Sacramento', 271: 'Salvador', 272: 'Samara', 273: 'San Antonio', 274: 'San Diego', 275: 'San Francisco', 276: 'San Jose', 277: 'San Salvador', 278: 'Santa Cruz', 279: 'Santiago', 280: 'Santiago', 281: 'Santiago', 282: 'Santo Domingo', 283: 'Santo Domingo', 284: 'Sarajevo', 285: 'Seattle', 286: 'Semarang', 287: 'Seoul', 288: 'Shanghai', 289: 'Shenyang', 290: 'Shenzhen', 291: 'Shiraz', 292: 'Singapore', 293: 'Skopje', 294: 'Sofia', 295: 'Soweto', 296: 'Stockholm', 297: 'Surabaya', 298: 'Surat', 299: 'Suzhou', 300: 'Sydney', 
    301: 'Tabriz', 302: 'Taiyuan', 303: 'Tallinn', 304: 'Tangshan', 305: 'Tashkent', 306: 'Tbilisi', 307: 'Tegucigalpa', 308: 'Tianjin', 309: 'Tijuana', 310: 'Tirana', 311: 'Tokyo', 312: 'Toronto', 313: 'Tripoli', 314: 'Tucson', 315: 'Tulsa', 316: 'Tunis', 317: 'Ufa', 318: 'Ulaanbaatar', 319: 'Vadodara', 320: 'Valencia', 321: 'Valencia', 322: 'Varanasi', 323: 'Victoria', 324: 'Vienna', 325: 'Vientiane', 326: 'Vilnius', 327: 'Virginia Beach', 328: 'Volgograd', 329: 'Warsaw', 330: 'Washington', 331: 'Wellington', 332: 'Wichita', 333: 'Windhoek', 334: 'Wuhan', 335: 'Wuxi', 336: 'Xian', 337: 'Xuzhou', 338: 'Yamoussoukro', 339: 'Yerevan', 340: 'Zagreb', 341: 'Zapopan'
}

local_data = pd.read_csv("city_data.csv")
global_data = pd.read_csv("global_data.csv")

local_data['ma_local'] = local_data['avg_temp'].rolling(window=20).mean()
global_data['ma_global'] = global_data['avg_temp'].rolling(window=20).mean()

local_data = (local_data.dropna()).reset_index(drop=True)
global_data = (global_data.dropna()).reset_index(drop=True)
st.title("⛅ Explore Weather Trends ⛅")
st.image("earth.png", width=700)

def format_func(option):
    return city_list[option]

def chart_func(local_col,global_col):
    fig = plt.figure()
    fig.patch.set_facecolor('#31333F')
    fig.patch.set_alpha(0)
    plt.plot(local_data['year'], local_data[local_col], label=f'{format_func(option)} temp', color= 'g')
    plt.plot(global_data['year'], global_data[global_col], label='Global temp', color= 'b')
    plt.legend()
    plt.xlabel('\nYear', color ="w")
    plt.ylabel('Temperature (°C)\n', color ="w")
    ax = plt.axes()
    ax.tick_params(colors='w', which='both')
    ax.set_facecolor("#31333F")
    return fig

st.markdown("<h2>Select the closest big city to where you live ..</h2>", unsafe_allow_html=True)

option = st.selectbox("", options=list(city_list.keys()), format_func=format_func)

col1, col2 = st.beta_columns(2)

with col1:
    option_data = local_data["city"].isin([format_func(option)])
    local_data = local_data[option_data]
    st.markdown(f"<h2>{format_func(option)} City Data</h2>", unsafe_allow_html=True)
    st.write(local_data)

    st.write("First Year:",local_data["year"].min())
    st.write("Last Year:",local_data["year"].max())
    st.write("Min Temp:",local_data["avg_temp"].min())
    st.write("Max Temp :",local_data["avg_temp"].max())

with col2:
    st.markdown("<h2>Global Data</h2>", unsafe_allow_html=True)
    st.write(global_data)
    st.write("First Year:",global_data["year"].min())
    st.write("Last Year:",global_data["year"].max())
    st.write("Min Temp:",global_data["avg_temp"].min())
    st.write("Max Temp :",global_data["avg_temp"].max())

    
fig1 = chart_func('avg_temp','avg_temp')
st.markdown("<h2>Weather Trends without Moving Average</h2>", unsafe_allow_html=True)
st.write(fig1)

fig2 = chart_func('ma_local','ma_global')
st.markdown("<h2>Weather Trends with Moving Average</h2>", unsafe_allow_html=True)
st.write(fig2)

st.markdown("<h2>Make observations about the similarities and differences between the world averages and your city’s averages, as well as overall trends. Here are some questions to get you started.</h2>", unsafe_allow_html=True)
st.markdown('''<ul>
               <li>Is your city hotter or cooler on average compared to the global average? Has the difference been consistent over time?</li>
               <li>How do the changes in your city’s temperatures over time compare to the changes in the global average?</li>
               <li>What does the overall trend look like? Is the world getting hotter or cooler? Has the trend been consistent over the last few hundred years?</li>
               </ul>''', unsafe_allow_html=True)

st.text_area("",height=220)

if st.button('Save As PDF'):
    config = pdfkit.configuration(wkhtmltopdf = r"D:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe") 
    pdfkit.from_url('http://localhost:8501', f'{format_func(option)}.pdf',configuration = config)

st.markdown("<h2 style='text-align: center;'>Made With 💖 By Amal Aljabri</h2>", unsafe_allow_html=True)    
