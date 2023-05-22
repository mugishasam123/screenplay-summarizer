import re
import nltk
import heapq  



script="our story today is called the boarded window it was written by Ambrose Bierce here is shop o'neill with the story . in eighteen thirty only a few miles away from what is now the great city of Cincinnati Ohio they are huge and almost endless forest . the area had %HESITATION few settlements established by people of the front two year many of them had already left the area for settlements further to the west but among those remaining was a man who had been one of the first people to arrive there . he lived alone in a house of logs surrounded on all sides by the great forest . he seemed a part of the darkness and silence of the forest for it no one had ever known him to smile or speak an unnecessary word . his simple needs were supplied by selling or trading the skins of wild animals in the town . his little log house had a single door . directly opposite was a window . the window was boarded up no one could remember a time when it was not . and no one knew why it had been close . I imagine there are few people living today whoever knew the secret of that window . but I am one . as you shall see . the man's name was said to be Marla . he appeared to be seventy years old but he was really fifty . something other than years have been the cause of his age . his hair and long full beard . is great lifeless ours . or some kind . his face was wrinkled . he was tall and thin with drooping shoulders like someone with many problems . I never saw him these details are it's learned from my grandfather he told me the man's story when I was a boy . he had known him when living nearby in that . early day . one day . Murdoch was found in his cabin . dead . it was not a time and place for medical examiners and newspapers I suppose it was agreed that he had died from natural causes or I should have been told kind should remember . I know only that the body was buried near the cabin . next to the burial place of his wife . she had died to so many years before him that local tradition noted very little of her existence . that closer as the final part of this true story . except for the incident that followed many years later . with a fearless spirit high you went to the place and got close enough to the ruins cabin to throw a stone against it I ran away to avoid the ghost which every well informed boy in the area new haunted the spot . but . there is an earlier part to this story . supplied by my grandfather . when murder lock built his cabin he was young . wrong and full of hope . he began the hard work of creating a farm . he kept the gun a rifle for hunting to support himself . he had married a young woman in all ways worthy of his honest love and loyalty . she shared the dangers of life with a willing spirit and a light heart . there is no known record of her name or details about her . they loved each other and were happy . one day Murdoch returned from hunting in a deep part of the forest he found his wife sick with fever and confusion there was no doctor or neighbor within miles she was in no condition to be left alone while he went to find help . so Murdock tried to take care of his wife and return her to good health . but . at the end of the third day she fell into unconsciousness and . diet . from what we know about a man like customer lock we may try to imagine some of the details of the story told by my grandfather . when she was sure she was dead . my luck had sense enough to remember that the dead must be prepared for burial . he made a mistake now and again while performing this special duty . he did certain things wrong . and others which she did correctly were done over and over again . he was surprised that he did not cry surprised and a little machine surely it is on kinds not to cry for the dead . tomorrow . he said out loud . I shall have to make the coffin and dig the graves and then I shall miss her when she is no longer in sight . but now . she is that of course . but it is all right it must be all right somehow . things cannot be as bad as they see . he stood over the body of his wife in the disappearing light he fixed the hair and made finishing touches to the rest . he did . all of this without thinking marked with care . and still through his mind ran a feeling that all was right that he should have her again as before and everything would be explained . Murdock had no experience and deep sadness his heart could not contained at all his imagination could not understand it . he did not know he was so hard Strock that knowledge would come later than never early . deep sadness is an artist of powers that affects people in different ways to one it comes like the stroke of a narrow shocking all the emotions to a sharper life to another it comes as the blow with a crushing strike . we may believe Murdock to have been affected that way . soon after he had finished his work he sank into a chair by the side of the table upon which the body lay . he noted how quite to his wife's face look in the deepening darkness he laid his arms upon the table's edge and dropped his face into them . two year less . and very sleepy . at that moment along screaming sound came in through the open window it was like the cry of a lost child in the far deep of the darkening forest but the man did not move he heard that on her cry on his feelings sense again nearer than before . may be it was a wild animal or maybe it was a dream . for . some . hours later . lifted his head from his arms and listened closely he knew not . there . in the black darkness by the side of the body he remembered everything without a shock he strained his eyes to see he knew not quiet . his senses were all alert his breath was suspended his blood was still as if to assist in the silence who what had awakened him and where was it . suddenly the table shook under his arms at the same time he heard or imagined he heard light soft step and then another the sounds were his bare feet walking up on the floor . he was afraid beyond the power to cry out or move . he waited . we sit there in the darkness through what seems like centuries of such fear . heroes one may know . but yet lived to tell . he tried but failed to speak the dead woman's name . I tried but failed to stretch his hand across the table to learn if she was there his throat was powerless his arms and hands were like land then . something most frightful happened seemed as if a heavy body was thrown against the table with a force that pushed against his chest at the same time he heard and felt the fall love something up on the floor it was so violent the crash that the whole house so . followed and the confusion of sounds impossible to describe . Murdock had risen to his feet extreme fear had caused him to lose control of his senses he threw his hands up on the table nothing . as they . there is a point at which fear it may turn to in sanity and insanity insights to action with no definite plans and acting like a mad man Murdoch ran quickly to the wall he sees his loaded rifle and without a name fired it . the flash from the rifle hit the room with a clear brightness he saw a huge ears panther tried getting the dead woman toward the window . wild animals T. . on her throne that . there was darkness blacker than before . when he returned to consciousness . the sun was high . and the forest was filled with the sounds of singing birds . the body lady near the window . where the animal had left it when frightened away by the light and sound of the rifle . the closing . zero in . the long hair was in this order . the arms and legs lady in a careless way . and a pool of blood flowed from the horribly torn throat . the reason he had used to tie the rifts . was broken . the hands were tightly closed . and . between the teeth . there was a piece of the animals . the boarded window was written by Ambrose Bierce it was adapted for special English by the one Davis who was also the producer . the storyteller worship the o'neill "

#Preprocessing


processed_movie = re.sub(r'\[[0-9]*\]', ' ', script)  
processed_movie = re.sub(r'\s+', ' ', script)

# Removing special characters and digits
formatted_movie = re.sub('[^a-zA-Z]', ' ', processed_movie )  
formatted_movie = re.sub(r'\s+', ' ', processed_movie)  

#Converting Text To Sentences

sentence_list = nltk.sent_tokenize(processed_movie)  
sentence_list


#Find Weighted Frequency of Occurrence

stopwords = nltk.corpus.stopwords.words('english')

word_frequencies = {}  
for word in nltk.word_tokenize(formatted_movie):  
    if word not in stopwords and word not in ".":
        if word not in word_frequencies.keys():
            word_frequencies[word] = 1
        else:
            word_frequencies[word] += 1
word_frequencies

#divide the number of occurances of all the words by the frequency of the most occurring word
maximum_frequncy = max(word_frequencies.values())

for word in word_frequencies.keys():  
    word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)
maximum_frequncy

#Calculating Sentence Scores

sentence_scores = {}  
for sent in sentence_list:  
    for word in nltk.word_tokenize(sent.lower()):
        if word in word_frequencies.keys():
            if len(sent.split(' ')) < 30:
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word]
                else:
                    sentence_scores[sent] += word_frequencies[word]
sentence_scores

#Getting the Summary


summary_sentences = heapq.nlargest(8, sentence_scores, key=sentence_scores.get)

summary = ' '.join(summary_sentences)  
print(summary) 