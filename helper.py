from urlextract import URLExtract
extract = URLExtract()

from wordcloud import WordCloud
import pandas as pd
from collections import Counter
import emoji


def fetch_stats(selected_user,df):

    if selected_user == 'Overall':

        num_of_messages = df.shape[0]
         
        words = []
        for message in df['message']:
            words.extend(message.split())

        media = df[df['message']=='<Media omitted>\n'].shape[0]

        links= []
        for message in df['message']:
            links.extend(extract.find_urls(message))

        return num_of_messages, len(words),media, len(links)
    
    else:

        new_df = df[df['user']==selected_user]
        num_of_messages = new_df.shape[0]

        words = []
        for message in new_df['message']:
            words.extend(message.split())

        media = new_df[new_df['message']=='<Media omitted>\n'].shape[0]

        links= []
        for message in new_df['message']:
            links.extend(extract.find_urls(message))

        return num_of_messages, len(words),media, len(links)


def most_busy_users(df):
    x = df['user'].value_counts().head()
    percent = round((df['user'].value_counts() / df.shape[0]) * 100, 2).reset_index().rename(columns={'index': 'name', 'user': 'percent'})
    return x,percent

def create_wordcloud(selected_user,df):

    f = open('stop_hinglish.txt','r')
    stop_words = f.read()

    if selected_user != 'Overall':
       df =  df[df['user']==selected_user]

    temp = df[df['user']!='group_notification']
    temp = temp[temp['message']!= '<Media omitted>\n']

    def remove_stop_words(message):
        y = []
        for word in message.lower().split():
            if word not in stop_words:
                y.append(word)
        return " ".join(y)


    wc = WordCloud(width=500,height=500,min_font_size=10,background_color='white')
    temp['message'] = temp['message'].apply(remove_stop_words)
    df_wc = wc.generate(temp['message'].str.cat(sep=" "))
    return df_wc

def most_common_words(selected_user,df):
    
    f = open('stop_hinglish.txt','r')
    stop_words = f.read()

    if selected_user != 'Overall':
       df =  df[df['user']==selected_user]

    temp = df[df['user']!='group_notification']
    temp = temp[temp['message']!= '<Media omitted>\n']
    
    words = []
    for message in temp['message']:
        for word in message.lower().split():
            if word not in stop_words:
                words.append(word)

    new_df = pd.DataFrame(Counter(words).most_common(20))

    return new_df


# timeline

def monthly_timeline(selected_user,df):
    if selected_user != 'Overall':
       df =  df[df['user']==selected_user]

    timeline = df.groupby(['year','month_num','month']).count()['message'].reset_index()
    
    time = []
    for i in range(timeline.shape[0]):
        time.append(timeline['month'][i] + "-" + str(timeline['year'][i]))
    timeline['time'] = time
    return timeline

def daily_timeline(selected_user,df):
    if selected_user != 'Overall':
       df =  df[df['user']==selected_user]

    daily_timeline = df.groupby('only_date').count()['message'].reset_index()

    return daily_timeline


def week_activity_map(selected_user,df):
    if selected_user != 'Overall':
       df =  df[df['user']==selected_user]
    return df['day_name'].value_counts()

def month_activity_map(selected_user,df):
    if selected_user != 'Overall':
       df =  df[df['user']==selected_user]
    return df['month'].value_counts()

def heat_map(selected_user,df):
    if selected_user != 'Overall':
       df =  df[df['user']==selected_user]
    user_heatmap = df.pivot_table(index='day_name', columns='period', values='message', aggfunc='count').fillna(0)

    return user_heatmap