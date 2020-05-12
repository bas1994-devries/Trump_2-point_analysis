import json
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
from better_profanity import profanity

f = open('../../gen/data-preparation/temp/trump_tweets.json','r', encoding='utf-8')
outfile = open('../../gen/data-preparation/temp/parsed-data.csv', 'w', encoding = 'utf-8')

con = f.readlines()
outfile.write('id\tcreated_at\ttext\tcompound\tpolarity\tpos\tneg\tprofanity\n')
tweet_list = []
pos_count = 0
neg_count = 0
cnt = 0
analyser = SentimentIntensityAnalyzer()

for line in con:
    if (len(line)<=5):
        continue

    cnt+=1
    obj = json.loads(line.replace('\n',''))
    text = obj.get('text')
    text = text.replace('\t', '').replace('\n', '')

    if text in tweet_list:
            continue

    out = analyser.polarity_scores(text)
    compound = out['compound']
    text_blob = TextBlob(text)
    polarity = text_blob.sentiment.polarity
    if not out['pos'] > 0.1:
        if out['pos']-out['neg'] < 0:
                neg_count += 1
                outfile.write(obj.get('id_str')+'\t'+obj.get('created_at')+'\t'+text+'\t'+str(compound)+'\t'+str(polarity)+'\t'+str(0)+'\t'+ str(1)+'\t'+ str(profanity.contains_profanity(text)) + '\n')
                tweet_list.append( text)

    if not out['neg'] > 0.1:
            if out['pos']-out['neg'] > 0:
                pos_count += 1
                outfile.write(obj.get('id_str')+'\t'+obj.get('created_at')+'\t'+text+'\t'+str(compound)+'\t'+str(polarity)+'\t'+str(1)+'\t'+str(0)+ '\t'+ str(profanity.contains_profanity(text)) + '\n')
                tweet_list.append( text)
    if cnt > 1500:
        break

    else:
        continue
f.close()
outfile.close()
print('1/2 done. Hannes & Hendrik are cool ;)')

##part WH briefing
f = open('../../gen/data-preparation/temp/whitehouse_briefing_27_04.json','r', encoding='utf-8')
outfile = open('../../gen/data-preparation/temp/parsed-data2.csv', 'w', encoding = 'utf-8')

con = f.readlines()
outfile.write('id\tcreated_at\ttext\tcompound\tpolarity\tpos\tneg\tprofanity\n')
tweet_list = []
pos_count = 0
neg_count = 0
cnt = 0
analyser = SentimentIntensityAnalyzer()

for line in con:
    if (len(line)<=5):
        continue

    cnt+=1
    obj = json.loads(line.replace('\n',''))
    text = obj.get('text')
    text = text.replace('\t', '').replace('\n', '')

    if text in tweet_list:
            continue

    out = analyser.polarity_scores(text)
    compound = out['compound']
    text_blob = TextBlob(text)
    polarity = text_blob.sentiment.polarity
    if not out['pos'] > 0.1:
        if out['pos']-out['neg'] < 0:
                neg_count += 1
                outfile.write(obj.get('id_str')+'\t'+obj.get('created_at')+'\t'+text+'\t'+str(compound)+'\t'+str(polarity)+'\t'+str(0)+'\t'+ str(1)+'\t'+ str(profanity.contains_profanity(text)) + '\n')
                tweet_list.append( text)

    if not out['neg'] > 0.1:
            if out['pos']-out['neg'] > 0:
                pos_count += 1
                outfile.write(obj.get('id_str')+'\t'+obj.get('created_at')+'\t'+text+'\t'+str(compound)+'\t'+str(polarity)+'\t'+str(1)+'\t'+str(0)+ '\t'+ str(profanity.contains_profanity(text)) + '\n')
                tweet_list.append( text)
    if cnt > 1500:
        break

    else:
        continue
f.close()
outfile.close()
print('done. Team 3 deserves a 10')
