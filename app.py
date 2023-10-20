import streamlit as st
from PIL import Image
import locale
from dataextraction import *
from transactions import *
from users import *
import plotly.express as plt
import plotly.graph_objects as go
import pandas as pd



image = Image.open('PhonePe-Logo.png')
page_title = 'PhonePe Pulse'
page_icon = image
layout = 'wide'

st.set_page_config(page_title=page_title,
                   page_icon=page_icon,
                   layout=layout
                   )


hide_style = '''
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            <style>
            
            '''
            
header_style = '''
             <style>
             .navbar {
                 position: fixed;
                 top: 0;
                 left: 0;
                 width: 100%;
                 z-index: 1;
                 display: flex;
                 justify-content: center;
                 align-items: center;
                 height: 80px;
                 background-color: #402866;
                 box-sizing: border-box;
             }
             
             .navbar-brand {
                 color: white !important;
                 font-size: 18px;
                 text-decoration: none;
                 margin-right: auto;
                 margin-left: 50px;
             }
             
             .navbar-brand img {
                margin-bottom: 6px;
                margin-right: 1px;
                width: 35px;
                height: 35px;
                justify-content: center;
            }
            
            /* Add the following CSS to change the color of the text */
            .navbar-brand span {
                color: #9973d5;
                justify-content: center;
            }
            
             </style>
             
             <nav class="navbar">
                 <div class="navbar-brand">
                <img src="D:\Data Science\Project-2\Phone-Pay.png" width="400" height="200" alt="">
                    PhonePe Pulse <span> | THE BEAT OF PROGRESS</span>
                 </div>
             </nav>
               '''
            
st.markdown(hide_style, unsafe_allow_html=True)

st.markdown(header_style, unsafe_allow_html=True)

selectbox_column, map_column, data_column = st.columns([1.5,2,2])


with selectbox_column:
    
    st.write("<style>div.row-widget.stButton > button {color: black !important;}</style>", unsafe_allow_html=True)

    st.button('All India', disabled=True)
    col4, col7 = st.columns([8, 8])

    with col4:
        options = st.selectbox("options", ('Transactions', 'Users'), key="options", label_visibility='collapsed')

    col5, col7 = st.columns([8, 8])
    with col5:
        year = st.selectbox("year", range(2018, 2023), key="year", label_visibility='collapsed')
        
    col6, col7 = st.columns([7, 7])

    with col6:
        quarter = st.selectbox("quarter", ('q1', 'q2', 'q3', 'q4'), key='quarter', label_visibility='collapsed')

with data_column:
    
    if options == 'Transactions':
        if year == year:
            if quarter == quarter:
                st.markdown('<h1 style="color: #402866; font-size: 37px;">Transactions</h1>', unsafe_allow_html=True)
                st.write('All PhonePe transactions (UPI + Cards + Wallets)')
    
                all_trans = (transactions(str(year), quarter)['All PhonePe transactions']).apply(lambda x: '{:,}'.format(x)).values[0]
                
                colored1 = f'<span style="color: #402866;font-size: 23px; font-weight: bold;">{all_trans}</span>'
                st.markdown(colored1, unsafe_allow_html=True)
                
                col8, col9 = st.columns([8,14])
                
                with col8:
                    st.write("Total payment value")
                    print(year,quarter)
                    print(transactions(year,quarter))
                    total_payment = transactions(str(year), quarter)['Total payment value'].apply(lambda x: '₹{:,.0f} Cr'.format(x/10000000)).values[0]
                    colored2 = f'<span style="color: #402866;font-size: 23px; font-weight: bold;">{total_payment}</span>'
                    st.markdown(colored2, unsafe_allow_html=True)
                with col9:
                    st.write("Avg. transaction value")
                    avg_trans = transactions(year, quarter)['Avg. transaction value'].apply(lambda x: '₹{:,.0f}'.format(x)).values[0]
                    colored3 = f'<span style="color: #402866;font-size: 23px; font-weight: bold;">{avg_trans}</span>'
                    st.markdown(colored3, unsafe_allow_html=True)
                
                col10, col11 = st.columns([12,12])
                    
                with col10:
    
                    st.markdown('<h1 style="color: #402866; font-size: 37px;">Categories </h1>', unsafe_allow_html=True)
                    st.write('Recharge & bill payments')
                    st.write('Peer-to-peer payments')
                    st.write('Merchant payments')
                    st.write('Financial Services')
                    st.write('Others')
                    
                with col11:
                    locale.setlocale(locale.LC_ALL, 'en_IN')
                    st.markdown("""<hr style="height:12.4px;border:none;color:#ffffff;background-color:#ffffff;" /> """, unsafe_allow_html=True)
                    recharge = transactions_categories(year, quarter)['Recharge & bill payments'].apply(lambda x: locale.format_string('%d', x, grouping=True)).values[0]
                    colored4 = f'<span style="color: #402866;font-size: 17px; font-weight: bold;">{recharge}</span>'
                    st.markdown(colored4, unsafe_allow_html=True)
                    
                    peer = transactions_categories(year, quarter)['Peer-to-peer payments'].apply(lambda x: locale.format_string('%d', x, grouping=True)).values[0]
                    colored5 = f'<span style="color: #402866;font-size: 17px; font-weight: bold;">{peer}</span>'
                    st.markdown(colored5, unsafe_allow_html=True)
                    
                    merchant = transactions_categories(year, quarter)['Merchant payments'].apply(lambda x: locale.format_string('%d', x, grouping=True)).values[0]
                    colored6 = f'<span style="color: #402866;font-size: 17px; font-weight: bold;">{merchant}</span>'
                    st.markdown(colored6, unsafe_allow_html=True)
                    
                    financial = transactions_categories(year, quarter)['Financial Services'].apply(lambda x: locale.format_string('%d', x, grouping=True)).values[0]
                    colored7 = f'<span style="color: #402866;font-size: 17px; font-weight: bold;">{financial}</span>'
                    st.markdown(colored7, unsafe_allow_html=True)
                    
                    others = transactions_categories(year, quarter)['Others'].apply(lambda x: locale.format_string('%d', x, grouping=True)).values[0]
                    colored8 = f'<span style="color: #402866;font-size: 17px; font-weight: bold;">{others}</span>'
                    st.markdown(colored8, unsafe_allow_html=True)
                    
    
                tab1, tab2, tab3 = st.tabs([' State ', ' District ', ' Pincode '])
                
                with tab1:
                    st.markdown('<h1 style="color: #402866; font-size: 25px;">Top 10 states</h1>', unsafe_allow_html=True)
                    col12, col13 = st.columns([8,14])
                    
                    with col12:
                        for rows in transactions_top_state(year, quarter)['State']:
                            state = rows.capitalize()
                            st.write(state)
                            
                    with col13:
                        for rows in transactions_top_state(year, quarter)['Total transaction count']:
                            if rows >= 10000000:
                                formatted_value = locale.format_string('%.2fCr', rows / 10000000, grouping=True)
                                colored9 = f'<span style="color: #402866;font-size: 16px; font-weight: bold;">{formatted_value}</span>'
                                st.markdown(colored9, unsafe_allow_html=True)
                            else:
                                formatted_value = locale.format_string('%.2fL', rows / 100000, grouping=True)
                                colored9 = f'<span style="color: #402866;font-size: 16px; font-weight: bold;">{formatted_value}</span>'
                                st.markdown(colored9, unsafe_allow_html=True)
                            
                with tab2:
                    st.markdown('<h1 style="color: #402866; font-size: 25px;">Top 10 districts</h1>', unsafe_allow_html=True)
                    col14, col15 = st.columns([8,14])
                    
                    with col14:
                        for rows in transactions_top_district(year, quarter)['District']:
                            district = rows.capitalize()
                            st.write(district)
                            
                    with col15:
                        for rows in transactions_top_district(year, quarter)['Total transaction count']:
                            if rows >= 10000000:
                                formatted_value = locale.format_string('%.2fCr', rows / 10000000, grouping=True)
                                colored10 = f'<span style="color: #402866;font-size: 16px; font-weight: bold;">{formatted_value}</span>'
                                st.markdown(colored10, unsafe_allow_html=True)
                            else:
                                formatted_value = locale.format_string('%.2fL', rows / 100000, grouping=True)
                                colored10 = f'<span style="color: #402866;font-size: 16px; font-weight: bold;">{formatted_value}</span>'
                                st.markdown(colored10, unsafe_allow_html=True)
                                
                with tab3:
                    st.markdown('<h1 style="color: #402866; font-size: 25px;">Top 10 pincodes</h1>', unsafe_allow_html=True)
                    col16, col17 = st.columns([8,14])
                    
                    with col16:
                        for rows in transactions_top_pincode(year, quarter)['Pincode']:
                            st.markdown(f"<span style='font-size: 16px;'>{rows}</span>", unsafe_allow_html=True)
                            
                    with col17:
                        for rows in transactions_top_pincode(year, quarter)['Total transaction count']:
                            if rows >= 10000000:
                                formatted_value = locale.format_string('%.2fCr', rows / 10000000, grouping=True)
                                colored11 = f'<span style="color: #402866;font-size: 16px; font-weight: bold;">{formatted_value}</span>'
                                st.markdown(colored11, unsafe_allow_html=True)
                            else:
                                formatted_value = locale.format_string('%.2fL', rows / 100000, grouping=True)
                                colored12 = f'<span style="color: #402866;font-size: 16px; font-weight: bold;">{formatted_value}</span>'
                                st.markdown(colored12, unsafe_allow_html=True)
            
    elif options == 'Users':
        if year == year:
            if quarter == quarter:
                st.markdown('<h1 style="color: #402866; font-size: 37px;">Users</h1>', unsafe_allow_html=True)
                st.write(f'Registered PhonePe users till {quarter} {year}')
                reg_usr = users(year, quarter)['Registered PhonePe users'].apply(lambda x: locale.format_string('%d', x, grouping=True)).values[0]
                colored13 = f'<span style="color: #402866;font-size: 23px; font-weight: bold;">{reg_usr}</span>'
                st.markdown(colored13, unsafe_allow_html=True)
                
                st.write(f'PhonePe app opens in {quarter} {year}')
                reg_usr = users(year, quarter)['PhonePe app opens'].apply(lambda x: locale.format_string('%d', x, grouping=True)).values[0]
                colored15 = f'<span style="color: #402866;font-size: 23px; font-weight: bold;">{reg_usr}</span>'
                st.markdown(colored15, unsafe_allow_html=True)
                
                tab4, tab5, tab6 = st.tabs([' State ', ' District ', ' Pincode '])
                
                with tab4:
                    st.markdown('<h1 style="color: #402866; font-size: 25px;">Top 10 states</h1>', unsafe_allow_html=True)
                    col18, col19 = st.columns([8,14])
                    
                    with col18:
                        for rows in users_top_state(year, quarter)['State']:
                            state = rows.capitalize()
                            st.write(state)
                            
                    with col19:
                        for rows in users_top_state(year, quarter)['Total registered users']:
                            if rows >= 10000000:
                                formatted_value = locale.format_string('%.2fCr', rows / 10000000, grouping=True)
                                colored16 = f'<span style="color: #402866;font-size: 16px; font-weight: bold;">{formatted_value}</span>'
                                st.markdown(colored16, unsafe_allow_html=True)
                            else:
                                formatted_value = locale.format_string('%.2fL', rows / 100000, grouping=True)
                                colored17 = f'<span style="color: #402866;font-size: 16px; font-weight: bold;">{formatted_value}</span>'
                                st.markdown(colored17, unsafe_allow_html=True)
                            
                with tab5:
                    st.markdown('<h1 style="color: #402866; font-size: 25px;">Top 10 districts</h1>', unsafe_allow_html=True)
                    col20, col21 = st.columns([8,14])
                    
                    with col20:
                        for rows in users_top_district(year, quarter)['District']:
                            district = rows.capitalize()
                            st.write(district)
                            
                    with col21:
                        for rows in users_top_district(year, quarter)['Total registered users']:
                            if rows >= 10000000:
                                formatted_value = locale.format_string('%.2fCr', rows / 10000000, grouping=True)
                                colored18 = f'<span style="color: #402866;font-size: 16px; font-weight: bold;">{formatted_value}</span>'
                                st.markdown(colored18, unsafe_allow_html=True)
                            else:
                                formatted_value = locale.format_string('%.2fL', rows / 100000, grouping=True)
                                colored19 = f'<span style="color: #402866;font-size: 16px; font-weight: bold;">{formatted_value}</span>'
                                st.markdown(colored19, unsafe_allow_html=True)
                                
                with tab6:
                    st.markdown('<h1 style="color: #402866; font-size: 25px;">Top 10 pincodes</h1>', unsafe_allow_html=True)
                    col22, col23 = st.columns([8,14])
                    
                    with col22:
                        for rows in users_top_pincode(year, quarter)['Pincode']:
                            st.markdown(f"<span style='font-size: 16px;'>{rows}</span>", unsafe_allow_html=True)
                            
                    with col23:
                        for rows in users_top_pincode(year, quarter)['Total registered users']:
                            if rows >= 10000000:
                                formatted_value = locale.format_string('%.2fCr', rows / 10000000, grouping=True)
                                colored20 = f'<span style="color: #402866;font-size: 16px; font-weight: bold;">{formatted_value}</span>'
                                st.markdown(colored20, unsafe_allow_html=True)
                            else:
                                formatted_value = locale.format_string('%.2fL', rows / 100000, grouping=True)
                                colored21 = f'<span style="color: #402866;font-size: 16px; font-weight: bold;">{formatted_value}</span>'
                                st.markdown(colored21, unsafe_allow_html=True)

with map_column:
    transactions = pd.read_csv(r'D:\Data Science\Project-2\CSV\geo_transactions.csv')
    users = pd.read_csv(r'D:\Data Science\Project-2\CSV\geo_users.csv')

    filtered_transactions = transactions[(transactions['Year'] == year) & (transactions['Quarter'] == quarter)]
    filtered_users = users[(users['Year'] == year) & (users['Quarter'] == quarter)]
    
    if options == 'Transactions':
        if year == year:
            if quarter == quarter:
                
                geojson_file = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
                
                transactions['State'] = transactions['State'].str.replace('and ', '& ')
                transactions['State'] = transactions['State'].str.replace('Andaman & Nicobar Islands', 'Andaman & Nicobar')
                
                figure = plt.choropleth(data_frame=filtered_transactions,
                    geojson=geojson_file,
                    featureidkey='properties.ST_NM',
                    locations='State',
                    projection='mercator',
                    hover_data={'Transaction_count': ':,', 'Transaction_amount': ':,'},
                    hover_name='State',
                    color_continuous_scale=plt.colors.colorbrewer.Set2,
                    scope='asia')
                figure.update_geos(fitbounds = "geojson",visible=False)
                figure.update_layout(margin={'r': 0, 't': 0, 'l': 0, 'b': 0})
                figure.update_layout(width=700, height=580)
                figure.update_layout(
                        geo=dict(bgcolor='rgba(0,0,0,0)'),
                        plot_bgcolor='rgba(0,0,0,0)', 
                        )
                        
        st.plotly_chart(figure, use_container_width=False)
                
    elif options == 'Users':
        if year == year:
            if quarter == quarter:
                
                geojson_file = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
                
                users['State'] = users['State'].str.replace('and ', '& ')
                users['State'] = users['State'].str.replace('Andaman & Nicobar Islands', 'Andaman & Nicobar')
                
                figure = plt.choropleth(data_frame=filtered_users,
                    geojson=geojson_file,
                    featureidkey='properties.ST_NM',
                    locations='State',
                    projection='mercator',
                    color='Registered_user',
                    hover_data={'Registered_user': ':,'},
                    hover_name='State',
                    color_continuous_scale=plt.colors.cyclical.Twilight,
                    scope='asia')
                figure.update_geos(fitbounds = "locations",visible=False)
                figure.update_layout(margin={'r': 0, 't': 0, 'l': 0, 'b': 0})
                figure.update_layout(width=500, height=550)
                figure.update_layout(
                    geo=dict(bgcolor='rgba(0,0,0,0)'),
                    plot_bgcolor='rgba(0,0,0,0)', 
                    )
                    
                st.plotly_chart(figure, use_container_width=False)
