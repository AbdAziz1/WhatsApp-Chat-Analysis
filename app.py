import streamlit as st
import preprocesser,helper
import matplotlib.pyplot as plt
import seaborn as sns

st.sidebar.title('WhatsApp Chat Analyzer')

uploaded_file = st.sidebar.file_uploader('Upload WhatsApp chat text file')
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    df = preprocesser.preprocess(data)

    #st.dataframe(df)

    #Fetching Unique Users

    user_list = df['user'].unique().tolist()
    user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0,'Overall')

    selected_user = st.sidebar.selectbox('show analysis wrt',user_list)

    if st.sidebar.button('Show Analysis'):

        num_messages,words,media,links = helper.fetch_stats(selected_user,df)

        st.title('Top Statistics')
        col1,col2,col3,col4 =  st.columns(4)
        with col1:
            st.header('Total Messages')
            st.title(num_messages)

        with col2:
            st.header('Total Words')
            st.title(words)

        with col3:
            st.header('Media Shared')
            st.title(media)

        with col4:
            st.header('Links Shared')
            st.title(links)
#monthly timeline
        st.title('Monthly Timeline')
        timeline = helper.monthly_timeline(selected_user,df)
        fig,ax = plt.subplots()
        ax.plot(timeline['time'],timeline['message'],color='green')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

#daily timeline

        st.title('daily Timeline')
        daily_timeline = helper.daily_timeline(selected_user,df)
        fig,ax = plt.subplots()
        ax.plot(daily_timeline['only_date'],daily_timeline['message'],color='black')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

#Activity map

        st.title('Activity Map')
        col1,col2 = st.columns(2)

        with col1:
            st.header('Most busy Day')
            busy_day = helper.week_activity_map(selected_user,df)
            fig,ax = plt.subplots()
            ax.bar(busy_day.index,busy_day.values)
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

        with col2:
            st.header('Most busy Month')
            busy_month = helper.month_activity_map(selected_user,df)
            fig,ax = plt.subplots()
            ax.bar(busy_month.index,busy_month.values)
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

#Heat Map
        st.title('Heat Map')
        user_heatmap = helper.heat_map(selected_user,df)
        fig,ax = plt.subplots()
        ax = sns.heatmap(user_heatmap)
        st.pyplot(fig) 


#Most Busy Users

        if selected_user == 'Overall':
            st.title('Most Busy Users')
            x,percent = helper.most_busy_users(df)
            fig, axis = plt.subplots()

            col1, col2 = st.columns(2)
            with col1:
                axis.bar(x.index, x.values,color = 'red')
                plt.xticks(rotation='vertical')
                st.pyplot(fig)
#Percentage of Users

            with col2:
                st.dataframe(percent)

#Word Cloud

        st.title('Word Cloud')
        df_wc = helper.create_wordcloud(selected_user,df)
        fig,ax = plt.subplots()
        ax.imshow(df_wc)
        st.pyplot(fig)

#Most Common Words

        most_common_df = helper.most_common_words(selected_user,df)
        fig,ax = plt.subplots()
        ax.barh(most_common_df[0],most_common_df[1])
        st.title('Most Common Words')
        st.pyplot(fig)

