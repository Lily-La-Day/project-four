from app import app, db
from models.writing import Writing
from models.edit import Edit
from models.final import Final
from models.final import FinalSchema
from models.writer import WriterSchema
from models.editor import EditorSchema
from models.category import Category, CategorySchema

writer_schema = WriterSchema()
editor_schema = EditorSchema()
final_schema = FinalSchema()
categogory_schema = CategorySchema()



with app.app_context():

    db.drop_all()

    db.create_all()

    work = Category(name='Work')
    formal = Category(name='Formal')
    business = Category(name='Business')
    personal = Category(name='Personal')
    poetry = Category(name='Poetry')
    prose = Category(name='Prose')
    formal_communications = Category(name='Formal Communication')
    complaint = Category(name='Letters of Complaint')
    cover_letter = Category(name='Cover Letter')
    CV = Category(name='CV')
    romance = Category(name='Romantic')
    enquiry = Category(name='Enquiry')
    suggestion = Category(name='Suggestion')
    criticism = Category(name='Criticism')
    journalism = Category(name='Journalism')
    blog = Category(name='Blog')
    short_story = Category(name='Short Story')
    fan_fiction = Category(name='Fan Fiction')
    family = Category(name='Family')
    thank_you = Category(name='Thank You/Gratitude')
    appreciation = Category(name='Appreciation/Praise')
    family = Category(name='Family')
    feedback = Category(name='Feedback')
    application = Category(name='Application')
    obituary = Category(name='Obituary')
    branding = Category(name='Branding')
    press_release = Category(name='Press Release')
    request = Category(name='Request')
    language = Category(name='Language')
    education = Category(name='Education')
    apology = Category(name='Apology')

    lily, errors = writer_schema.load({
        'username': 'lily',
        'email': 'lily@email',
        'password': 'pass',
        'password_confirmation': 'pass'
    })

    tom, errors = writer_schema.load({
        'username': 'tom',
        'email': 'tom@email',
        'password': 'pass',
        'password_confirmation': 'pass'
    })

    sheema, errors = writer_schema.load({
        'username': 'sheema',
        'email': 'sheema@email',
        'password': 'pass',
        'password_confirmation': 'pass'
    })

    amy, errors = writer_schema.load({
        'username': 'amy',
        'email': 'amy@email',
        'password': 'pass',
        'password_confirmation': 'pass'
    })

    kasia, errors = writer_schema.load({
        'username': 'kasia',
        'email': 'kasia@email',
        'password': 'pass',
        'password_confirmation': 'pass'
    })

    ola, errors = writer_schema.load({
        'username': 'ola',
        'email': 'ola@email',
        'password': 'pass',
        'password_confirmation': 'pass'
    })

    charlie, errors = writer_schema.load({
        'username': 'charlie',
        'email': 'charlie@email',
        'password': 'pass',
        'password_confirmation': 'pass'
    })

    jack, errors = writer_schema.load({
        'username': 'jack',
        'email': 'jack@email',
        'password': 'pass',
        'password_confirmation': 'pass'
    })

    wes, errors = writer_schema.load({
        'username': 'wes',
        'email': 'wes@email',
        'password': 'pass',
        'password_confirmation': 'pass'
    })

    shane, errors = writer_schema.load({
        'username': 'shane',
        'email': 'shane@email',
        'password': 'pass',
        'password_confirmation': 'pass'
    })

    talha, errors = writer_schema.load({
        'username': 'talha',
        'email': 'talha@email',
        'password': 'pass',
        'password_confirmation': 'pass'
    })

    mia, errors = writer_schema.load({
        'username': 'mia',
        'email': 'mia@email',
        'password': 'pass',
        'password_confirmation': 'pass'
    })

    daniela, errors = writer_schema.load({
        'username': 'daniela',
        'email': 'daniela@email',
        'password': 'pass',
        'password_confirmation': 'pass'
    })

    sim, errors = writer_schema.load({
        'username': 'sim',
        'email': 'sim@email',
        'password': 'pass',
        'password_confirmation': 'pass'
    })

    gae, errors = writer_schema.load({
        'username': 'gae',
        'email': 'gae@email',
        'password': 'pass',
        'password_confirmation': 'pass'
    })

    cliff, errors = writer_schema.load({
        'username': 'cliff',
        'email': 'cliff@email',
        'password': 'pass',
        'password_confirmation': 'pass'
    })

    brendan, errors = writer_schema.load({
        'username': 'brendan',
        'email': 'brendan@email',
        'password': 'pass',
        'password_confirmation': 'pass'
    })

    ollie, errors = writer_schema.load({
        'username': 'ollie',
        'email': 'ollie@email',
        'password': 'pass',
        'password_confirmation': 'pass'
    })

    kelsey, errors = writer_schema.load({
        'username': 'kelsey',
        'email': 'kelsey@email',
        'password': 'pass',
        'password_confirmation': 'pass'
    })

    olli, errors = writer_schema.load({
        'username': 'olli',
        'email': 'olli@email',
        'password': 'pass',
        'password_confirmation': 'pass'
    })








    if errors:
        raise Exception(errors)

    ollie, errors = editor_schema.load({
            'username': 'ollie',
            'email': 'ollie@email',
            'password': 'pass',
            'password_confirmation': 'pass'
        })

    if errors:
        raise Exception(errors)

    lindsay, errors = editor_schema.load({
            'username': 'lindsay',
            'email': 'lindsay@email',
            'password': 'pass',
            'password_confirmation': 'pass'
        })

    anna, errors = editor_schema.load({
            'username': 'anna',
            'email': 'anna@email',
            'password': 'pass',
            'password_confirmation': 'pass'
        })

    lindsay, errors = editor_schema.load({
            'username': 'lindsay',
            'email': 'lindsay@email',
            'password': 'pass',
            'password_confirmation': 'pass'
        })

    laura, errors = editor_schema.load({
            'username': 'laura',
            'email': 'laura@email',
            'password': 'pass',
            'password_confirmation': 'pass'
        })

    harry, errors = editor_schema.load({
            'username': 'harry',
            'email': 'harry@email',
            'password': 'pass',
            'password_confirmation': 'pass'
        })

    alex, errors = editor_schema.load({
            'username': 'alex',
            'email': 'alex@email',
            'password': 'pass',
            'password_confirmation': 'pass'
        })


    if errors:
        raise Exception(errors)

    writing_one = Writing(
    title='A pome what I have wrote 4 u',
    text='"I am jell the small parts of the rock that surronds you around you what do the flashes \n women  \n do without alot of lugage \n glue \n before they reprsent it. Gods fingers, tares and tares of small fury tings, wat today seems to be flowers are not to make pome by HIMSELF and have not lost it yet.',
    categories=[romance, personal],
    author=tom
    )
    writing_two = Writing(
    title='Making waves over plane flight to Bad bad BA',
    text=' Then, after 1919, I was on a two-way trip from Cape Town to London. Enter 11 hours for entertainment online as you know. Our service was very difficult during the visit and it was very difficult to make it popular. The hotel is north of BA 20. After live activity, we found that education systems were not working. We started, but the police told us that they were working with this system after the Greg Underview system. After trying to spend from three minutes to 45 minutes, I heard many passengers know what to do in this way. Among them are vampires, grief and protection of our work, especially in Medelia and Phillip. I heard the passers-by saying that the situation was unfair and that they were undaunted. Each member has more accidents for two hours and has never been found. Eventually, Greg talked to any influential person and apologized for the matter. I told you that we understood that his staff were inaccurate, and we hoped them. We complained and told us to get the payment. I wish to talk about success, this was a stunning reaction to the BA 11, confirming that the plane was "very difficult" and "all", but when it was upset, British airlines reduced their scientific practices. Their rates are on the seats. We provide basic needs. In the 11th and 11th days, when the merchant returned to the boat, he was a seller who sought the passengers and knew basic needs, such as alcohol. At the end of the trip, Matilda\'s guests took a few steps. However, some of the features given to us were taken away and they were gone. Then, Filipp\'s tea. They were delighted, and Phillip responded, I did not find my suggestions on looking up or working.At the same time, during the sale, I heard something strangely unusual about other foods. It\'s a bad experience to start from the beginning to 20 years.',
    categories=[business, formal, complaint, feedback, suggestion],
    author=sheema
    )
    writing_three = Writing(
    title='Let Me wrk in ur Bar!',
    text='Appleby: You can be able to read a new subscription. Apart from everyday business opportunities, good works of teamwork and guidance, I have been made good like from the MithIntyre Bar and Grill. The General Discussion n chit chat and that of your own experiences, gardens, wars and spirits, and for preparing some of the ready trades for this type of role. Competition management, administration and managmnt of peeple ho are able to do this. I can do educaton skills to protect a clean and secure environment, and have the right to communicate and talk and manage the time. Mines: Minor residents of mine acceptance and acceptance of food items, save food and drink, pay money and make money, protect and transfer money. It also has many rectangular functions. Help assist executive executives create whole-hearted business services and improve the health care needs. Building myself and planning, specialty management and specialty specialty specialties and tips for business staff and new consumer food. If I have a new experience of experience, my strength, New York\'s capabilities and discrimination, I would like to show my role in my role. I hope this ocupation is good!!!!!! cherrs, hamish Horesdale',
    categories=[work, cover_letter, CV, formal, application, business, request],
    author=sim
    )
    writing_four = Writing(
    title='Wedding Thank You',
    text='This letter describes the action taken regarding complaints of sexual harassment against John Doe. Mr. Doe was notified by letter of the complaints, and he met with me April 12 for further discussion of the matter. We reviewed the specific nature of each complaint originating in the accounting department and carefully examined company policy on each issue. Mr. Doe was informed that his employment with Doe Corporation would be terminated if more substantiated complaints of this nature were received. He has agreed to attend classes given by the human resources department to help him be more aware of the types of behaviors that may be offensive to others.',
    categories=[personal, family, thank_you],
    author=mia
    )
    writing_five = Writing(
    title='Valentins Poem',
    text='If u wer crazy, I\'d go out in the sun. I run the tor late at nite so I can keep it in good lite. If u r in my world, I hav da lite of nite, the silent boundry, the dark of fortnite. Are 2 groups sumtimes turn are dances into dances. If you are on my island, I will be on my bitch and keep the see slow and tidy. This series contains sand dunes, but now with the storm I luv the soft vew. If u promiss 2 luv, I will be on time. But we are manz, but this is the luv of lurve, and this is my forever not to pie u Valentine.',
    categories=[romance, personal, family],
    author=shane
    )
    writing_six = Writing(
    title='PA Application',
    text='Dear Felix, SUP DUDE? On behalf of my representative, I love you and everyting you do and I believe in myself. When a service is issues, the man says he needs a person to assist him in both aspects of the project. My current role as auxiliary support. I am a key player between my team and team so that I can focus on minimizing activities my chance to reduce self and reduce my choices. To continue this activity, you will learn to benefit others. Wechsler 7% class. It also uses direct connection with meetings, meetings, and preparation of the man. This file is recommended for advisory plans when discouraged. Thank you for reviewing your application. Lots of love, Elena Bizanthrope',
    categories=[work, business, CV, cover_letter, application],
    author=talha
    )
    writing_seven = Writing(
    title='Brand Statement',
    text='A money maker money making boss- THAT\'S WHAT I AM!, I offer flexibility and MONEY MAKING to make things go bOOM BOOM BOOM, enabling staff to make so much MONEY. Seriously, I AM SO GOOD.',
    categories=[business, formal, work, CV],
    author=ola
    )
    writing_eight = Writing(
    title='Burger Complaint',
    text='Oh come on this is ridic! I went to restaurant at 341 Hampton Rd. Friday, June 6. We arrived at 11.45. Ihave the invoice as proofo youeah??? so deon\t deny it!!! This is the nearest office. We met at least five times last year. Our Friday experience was a no brainer. We are not satisfied with chastity and curiosity. All the garbage tables are dirty and full of junk and junk. In addition, the house cleans the floor. The bathroom is not very clean. Previously, the restaurant was clean. We enjoyed Tacos joy. Mabes if you make things better. We usually visit at least once a month. Hide me. Thanks for the answer. Hi to you, William McPurry',
    categories=[complaint, formal, business, suggestion, criticism, feedback],
    author=kasia
    )
    writing_nine = Writing(
    title='Dance Teacher Cover Letter',
    text='My inspo for dance lessons came from the same affect that leaded me to my dance career nearly 13 years ago." Since the start place of my education in the artistic things, I have tried to use the language of the body to tell stories And feeling in the new language, and I became a strong supporter of teaching others. Throughout my career, I have seen dancing One to increase the life of dance and drama, and as my dad, I see students learn different kinds of dance and follow their creative expression, believe in fake compliments. Dancing is the first experience to develop the perspective of people who are interested in creating their own experience of creative, creative and creative. Believe me. Attempting my experience is related to ... A group of dancers ages 4 to 14 yrs old as a young dancer, Beck Cred studio studio. Dance and activities make the students happy!!!!! Introduce tips, music and music for students to experience.  In giving information about the dance style Adults with a fascinating story and discussion by using various teaching methods for each group. Manage different administrative tasks, including parental, scheduling, and payment communications. I got my MFA to dance at the MFA College and an introductory level in Natural Dance as a graduate assistant. San Francisco Spark Temp has been working for 13 years as a painter, artist, journalist and guest speaker (for a complete list of testimonials and art available upon request). My deep experience as a professional dancer and to inspire new and varied singers, I have successfully delivered Chrysalis Dance. I look forward to discussing my position and my advantages. Thanks for your attention. \n \n Lots of Love, Martha Greenpark',
    categories=[work, CV, application, business, formal_communications, formal, request],
    author=mia
    )
    writing_ten = Writing(
    title='Cadburys WTAF??????',
    text='I do not want to beleeve that the last choclate bar has a different taste, so it\'s different, so I look online to see how other people have had a lot of negging after changing the same formula. iv eaten this choc long time, Im not interested now! I have a little pie for a cup ... I willn\'t buy another brand from now on to find D The correct formula is no different, and it does not break with the dark chocolate.',
    categories=[formal, feedback, complaint, business],
    author=charlie
    )
    writing_eleven = Writing(
    title='Waiter Misconduct Complaint',
    text='Dear Sir, I went to the restaurant on September 10, 2013 for dinner with my family. We ordered Chinese food and saved the waitress in early spring. If you wait a long time, your browser has expired. He reported this to his boss, but he was shocked when he refused to acknowledge and said he should find another restaurant. The children started to complain about the wrongs and we took them to the hospital. Your doctor has reported a food poisoning. Timely medical care. We encourage you to investigate your merits and cheats and take action on your service personnel. I will send you a copy of the invoice asking you to return the case. Thanks (or not!)',
    categories=[formal, feedback, complaint],
    author=tom
    )
    writing_twelve = Writing(
    title='Junior Web Developer Cover Letter',
    text='TLDR? HIRE ME, HERE IS WHY! I AM SO GOOD WITH COMPUTERS AND KNOW LOTS!!!!!!! \n \n \n Use the article for information about this article and the best information for your information. If you like checking / XML / PLSL, look for product support? Send cable that requires product support. You can get a lot of products in the best place for new service languages ​​and you can get a character for it. Click here to see this article in this article for more information about your name or name targeting visually. We can post this article for your article in protecting your website. We can post this article for more information on this article. Click here to see this article in Germany. In the past five years, an exclusive article in the best place has the best position in the Internet language. Log in to your Account Manager. You can log in to your Account Manager. We can get this article on the web. Bracken Mist Hadden ',
    categories=[work, application, business, CV],
    author=jack
    )
    writing_thirteen = Writing(
    title='English Practiss Advert',
    text='I want  meet someone who will do English, I do vietnamese and now do not have a great experience!',
    categories=[language, education],
    author=jack
    )
    writing_fourteen = Writing(
    title='MY STARTUP!!!!!!',
    text='Known and combined fruits with eleven new products from around the world, Delley Wesley Adapters, Walnut, Coconut Oil and Glasses are the 11 new ones to choose from. a wide range of branded products, launched exclusively in the Western markets of 2012, and will highlight new results in the coming months with almond oil cashew and cashew oils and extra 28 White oil. Walnuts Wesley Gold, co-founder of Wesley Gold, said: "I am very pleased to introduce Walnut Petroleum Products to a Southwest Company." "We gave 11 new products, not just one but two new nut fruits, fresh scents, and fresh ingredients that distinguish fruits and sugar. Wait until you get the Maphe Cashew taste." My bones are my new favorite creation!',
    categories=[business, formal, branding, press_release, journalism],
    author=wes
    )
    writing_fifteen = Writing(
    title='Grannys Obitchuary',
    text='Ms Margaret, who has lived in the Hull area for a long time, died Wednesday, May 18 at Sun Bridge Health Center. In 1928 Hull, SD, Margaret received her Bachelor of Science in Nursing from Hull University School of Medicine in 1991. She continued her education at Hull University, where she attended. Received his MD in Nursing in 1955. Margaret enrolled at Hull University in Amsterdam in the mid-1960s and worked in nursing homes in Massachusetts in 1970. She received a post as a librarian at Hull University of Technology. County, where he worked until his retirement. Margaret loves good food and flowers, enjoys movies and games with friends, and has a great smile that can shine in a room. Her grandmother, Tablia Winslow and many of her grandparents, all living in south Hull, have fun in the coming years. Memories can be a gift to human society in the Eternal Cave. Douglas work, stop slot.',
    categories=[personal, formal, obituary, journalism],
    author=cliff
    )

    writing_sixteen = Writing(
    title='news paper artical for advertising as you like it',
    text='The Theater People are so happy to announce a version of  As You Like It Against the Background of New York City during the Great Depression. He held court-appointed discontent presentations for Hooverville from Arden, Rosalind, Orlando and their colleagues making love and talking about class conditions in a war place. Working words, music, and a pair of very very very very  comics make it one of Shakespeare\'s favorite hilarious plays',
    categories=[journalism, press_release, formal, branding ],
    author=gae
    )

    writing_seventeen = Writing(
    title='so so so so sorry',
    text='I feel that you really deserve massive sorry! Personal apologies for the meeting yesterday. I know these days because I\'m sorry. I hope you can forgive me. I have a great honor to work with you. Sorry. Sorry Please ...',
    categories=[formal, apology, personal, work, business],
    author=jack
    )
    writing_eighteen = Writing(
    title='MY STARTUP!!!!!!',
    text='On the morning of June 27, the heat was clear all summer. Too much peace and green grass. The man stopped for ten minutes at the post office and the bank. Many people started working in the city on June 2 for two days. There were only three hundred people living in rural areas and the crisis went down for two hours, so that the morning started at ten and the villagers needed food. After the chat boy. It was a summer school and often surrounded his independence and quickly started working. And teachings on class and teacher, books and titles. Bobby Martin picked up his stones and quickly and easily received other children to get the most beautiful and bright stones. Bobby and Harry Jones and Dickie Dellcrovey - people in the village say - have finally been built in forest areas and other children protected by the ceasefire. Boys are different, talking, looking at their stones, robbing or becoming strangers to their ancestors. Talk about kids, forests and mountains, tractors and tax collection early. They stood around the rock, gathered around the boat, replaced instead, were quiet and quiet. Womens clothing and bedding are near their time.',
    categories=[business, formal],
    author=wes
    )
    writing_nineteen = Writing(
    title='Letter on front of job app',
    text='I noticed that my inbox (embarrassing!!!!!) holds 150000000 unread messages, including at least 5000 different type newsletters. But this only creates an email that is worth the opening. In my opinion, the use of your job is a real advantage. I\'ve been following Vitabe for a number of years, and I can say that I\'ll return any email you send me. I have a good cube for a good subject line - "Vitamin A is over - our favorite thing with ABC with my" favorite "- and how your email content feels fun and expert help, talking for the reason I I am glad to present your request to the email marketing email address of your company, I have four years of marketing experience, my current role at West Side Bank is to provide email designs. New data for new customers is analyzed and Analyze data on different types of customers that change with people who have already received money, as well as the results of the A / B survey and tourism maps. We interacted, we were able to pay. And 30% of these subscribers, as our result would be significantly higher than last year, I also focused on credit reports to educate my clients about How they manage and manage their records that have the highest record',
    categories=[work, business, application, formal, CV, cover_letter],
    author=cliff
    )

    writing_twenty = Writing(
    title='Harry Potter Fan Fiction',
    text='Albus moved under his blankets. His leg was torn off his plate (how did this happen?), And he sat in his bed, so that sunlight flowed through his window. She looked at art, who slept slowly in a sleeping bag on the floor. How did the person get the best sleep on earth? Albus felt sweaty and sad. His neck bent slightly. He must have laughed at her. Al up and down stairs, where mom and James ate breakfast. Her usual home is boring - she left yesterday Atlantis, after a day trip around the city. "I think Father and Lily are still sleeping?" Albus asked: He is tied up in the chair.  "Indeed, neither is Lily still asleep, but your father at work, the mother answered." But I thought Dad with us came to Diagon\'s Alley today! "It\'s their program they have two days in the World Cup, the next day It started on Diagon alley, and then art to school, but your Dad wanted to go with them on the Diagon , which was supposed to fall with us, but at an hour after this second morning, your father "What happened to you?" "What did he say to you?" James asked enthusiastically: "We do not say that they still do not know much. There was no strong evidence from this morning.""A strong certificate From what? " James asked, "Come on, mother, please?" Albus asked what was exciting to drag her father in the morning of her Diagon alley trip. Probably you will see the evening prophet tonight tonight. Oh, so, enough for the Prophet\'s version of the important era? "It\'s possible that the exciting news that was published during the day that the Prophet Muhammad was published the next morning," James excited. Otherwise, surely it will be on the morning of the day. So you have to fill your breakfast today. Aunt Hermione, Rose, and Hugo in the liquid kettle this morning, right? about two hours, I think." Albus noted, they ate slowly for a few minutes. Albus left a glass of orange juice and wasted away from eating his own bread.',
    categories=[fan_fiction, prose, short_story ],
    author=gae
    )
    edited_one = Edit(title='For You', original=writing_one,
    text='I am jealous of the sand\n beneath you \n around you \n what you see \n bright things \n  erased lady \n sparkling and traveling without luggage \n liquidity \n before X \n you are tattooed on my back \n music \n dies down \n I too grew up in \n the soft hands \n of the gods \n and a little donkey will lead them \n Tears, tears, and I know \n just what they mean \n honeysuckles at night \n  I wrote this poem for you and haven\'t lost it',
    editor=lindsay,
        liked_by=[anna, lindsay, ollie, alex, harry, laura],
        rating=4)

    edited_two = Edit(title='Letter of Complaint to British Airways', original=writing_two,
    text='To whom it may concern, \n \n I am writing to complain about our flight from Cape Town to London Heathrow on 19/04/19.  As you will be aware, our in-flight entertainment did not work for the entirety of the 11-hour flight. Our cabin crew were rude and unhelpful throughout the flight, making it a hugely unpleasant experience. I am extremely disappointed with the £20 voucher response and do not think this is sufficient compensation for the errors made by BA. \n \n After immediately boarding the place, we noticed that the in-flight entertainment system was not working. We had not yet taken off, but the cabin crew informed us that it was only possible to do a system reset after take-off. We were told that this would resolve the issue.  Greg Underwood, the Customer Relations Manager, asked that we let her know if the system reboot had not worked. After three attempts, and nearly 45 minutes without being updated, I heard several other passengers asking the cabin crew if the issue would be resolved. They were met with annoyance, frustration and a defensive attitude from our cabin crew - namely, Matilda and Phillip. I heard Matilda say to the inquiring passenger that the situation was “unfair” on staff and she walked away without apologising.  Both members of the cabin crew ignored the issue for over two hours and we had still not received an apology. \n \n Eventually, Greg spoke with each row of affected passengers and apologised for the issue. I informed her that we felt as if cabin crew had ignored the situation and that more could have been done to apologise.  We received the complaints leaflet and were informed we would receive compensation. \n \n I would like to take the opportunity here to add that while she was speaking to a passenger behind me, who had spent the previous 11-hour BA flight with broken screens, Greg admitted that the plane was “very old” and that the screens “break all the time”. In an era where low-cost flights are readily available, passengers choose to pay extra for the reputation and comfort of British Airways. I am shocked and appalled that a company with the reputation of British Airways would knowingly allow for passengers to spend their money on seats that do not have the basic amenities that we pay for. \n \n In addition to the broken screens during the entirety of our 11-hour flight, the cabin crew were rude and unpleasant to my family and to other passengers around her. Phillip in particular was evidently very unhappy. Throughout the flight, she snapped at passengers and did not offer to help with our basic requests, such as drinks.  At the end of the flight, Matilda was pouring coffee for passengers. However, she stopped a few rows ahead of ours and did not return. A while later, Phillip returned with tea. The passengers in the row behind asked politely for coffee, to which Phillip replied, “Coffee has already been down here”. She did not offer to get more or apologise for the fault of the cabin crew.  As well as this, during the flight, I heard another passenger become very upset because her meal had not been put on to the plane. \n \n It is clear that both the cabin crew and the plane were not prepared for the flight. It was horrible experience from start to finish and one that absolutely requires more than a £20 voucher to compensate. \n \n I look forward to hearing your response and your suggestion for a more suitable compensation for all four members of my party.',
    editor=alex,
        liked_by=[anna, lindsay, ollie, alex, harry, laura],
        rating=4)

    edited_three = Edit(title='Bar Job Application', original=writing_three,
    text='Miss Appleby: After reading about your need to be a new member, you can join me. In addition to providing excellent clients with casual and classy dining experiences, having a good knowledge of team collaboration and leadership, I greatly benefit from this role at McIntyre Bar and Grill. General Discussion \n My experience in preparing and transporting cocktails, beer, wine and spirits to different clients has prepared for this role. My ability to achieve this capability is government preparation, inventory management, and managing people. I can produce faulty alcohol while maintaining a clean and safe environment, and have the ability to interact and communicate and manage time. Examples of my background are: The Hygiene Line takes customers and orders, delivers the right food and drink, collects and makes money, maintains excellent inventory levels, and quickly. It also balances several restaurant functions. enables managers to create a full range of operational tasks and provide better customer satisfaction support. \n Demonstrate team building and planning skills, strong leadership skills and unique interpersonal skills, tips for new employees in regular bar and restaurant operations. If my past experience and enthusiasm and ability, and the neutrality of New York, I would like to highlight my expectations for this role. I look forward to discussing this post in more detail. Thanks for looking. \n Unfortunately, Horsehead',
    editor=lindsay,
        liked_by=[anna, lindsay, ollie, alex, harry, laura],
        rating=20)

    edited_four = Edit(title='A Wedding Thank You', original=writing_fourteen,
    text='“From the bottom of our hearts we would like to thank you for celebrating our special day with us and making it the most memorable day of our lives. From sweating it out together during the ceremony, to dancing the night away in the rain, we definitely felt the love from you all on the day. \n \n We can’t wait for our trip to Europe at the end of July, which wouldn’t be possible without all of your generous gifts.\n \n We look forward to starting the next chapter of our lives together and sharing many more memories with you all!”',
    editor=lindsay,
        liked_by=[anna, lindsay, ollie, alex, harry, laura],
        rating=20)

    edited_five = Edit(title='Valentine', original=writing_five,
    text='If you were crazy, I\'d go out in the sun. I run the tour late at night so I can keep it in good light. If you are in my world, I have the light of night, the silent boundary, the dark of night. Our two groups sometimes turn our dances into dances. If you are on my island, I will be on my beach and keep the sea slow and tidy. This series contains sand dunes, but now with the storm I love the soft view. If you promise to love, I will be on time. But we are human, but this is the love of love, and this is my forever faithful Valentine.',
    editor=anna,
        liked_by=[anna, lindsay, ollie, alex, harry, laura],
        rating=6)

    edited_six = Edit(title='Application For Position of Personal Assistant', original=writing_six,
    text='Dear Mr Darling, \n \n Please find enclosed my application for the role of personal assistant. I found your job posting on indeed.com , and I believe that my experience and skills make me the perfect candidate for this position. \n \n Your job posting states that your company’s CEO requires an experienced personal assistant to support her in all aspects of her work. \n \n In my current role as personal assistant to Ms. Miseldoon, CEO of Blue & White, I act as the primary gateway between her and her team, ensuring that she can focus on the tasks that require her personal attention while minimizing the scope for distractions. In this way, I have successfully increased Ms. Wexler’s productive time by 7%. \n \n Additionally, I harness my communication and interpersonal skills to liaise between departments, scheduling team meetings and conference calls for Ms. Romper. Because of my ability to multitask, Ms. Hale has entrusted me with keeping minutes for such meetings. \n \n I also spearheaded Blue & White’s 10-minute stand-up meeting initiate that has boosted workplace efficiency by reducing wasted time. \n I am looking forward to hearing back from you. Thank you for considering my application. \n \n Sincerely, \n \n Felina Bysanthrope',
    editor=anna,
        liked_by=[anna, lindsay, ollie, alex, harry, laura],
        rating=9)

    edited_seven = Edit(title='PBS', original=writing_seven,
    text='An entrepreneurial and entrepreneurial leader, I offer flexibility and entrepreneurship to foster good growth and good entrepreneurship, enabling staff to achieve high production. And increase a business, trustworthy and trustworthy. My plan for managing calm is to make people better understand, proud, and motivated to become the best in the industry.',
    editor=anna,
        liked_by=[anna, laura],
        rating=9)
    edited_eight = Edit(title='Letter of Complaint to Fast Food Establishment', original=writing_fourteen,
    text=' Dear Mrs. Artengrowth, \n \n My coworkers and I recently visited the Mysterious Meat restaurant at 341 Hampton Rd. on Friday, June 6th. We arrived at about 11:45. I have enclosed a copy of my receipt for your convenience. \n \n This location is close to our office. We have met there at least five times within the past year. However, our experience on Friday was not a positive one. We were unhappy with the cleanliness and felt you needed to be made aware of the situation. All of the unoccupied tables were dirty and littered with crumbs and trash. In addition, the floor appeared to need mopping. The bathrooms were not very clean as well. \n \n In the past, the restaurant has been clean. We really do enjoy the food at the Happy Taco. If improvements are made, we would be more likely to meet there again in the future. We typically visit at least once a month. \n \n Please feel free to contact me. Thank you for your response. Have a good day. \n \n Sincerely, \n \n Willam Makepeace',
    editor=anna,
        liked_by=[anna, laura],
        rating=9)
    edited_nine = Edit(title='Dance Teacher Cover Letter', original=writing_nine,
    text='My motivation to teach dance derives from the same impulse that led me into my fulfilling dance career nearly 13 years ago. Since the beginning of my studies in the performing arts, I have sought to use physical movement to express stories and emotions in innovative ways, and I am a strong proponent of teaching others how to do the same. Throughout my career, I have consistently viewed dance as a way to enrich both performers’ and viewers’ lives, and I believe my obligation as a dance teacher is to encourage students to learn a variety of dance styles and pursue their own creative expression. Having experienced first-hand the power of dance to shape people’s perspectives, I am enthusiastic about using my professional experiences, skills, and beliefs to educate new young dancers in the techniques and movements of creative dance. \n \n Highlights of my experience include… \n \n Leading groups of young dancers ranging in age from 4 to 14 for the past six years as an instructor with the Berkeley Dance Studio; demonstrating dances and movements, making suggestions to students, monitoring performance, and introducing new artistic and musical elements to keep students engaged and excited. \n \n Applying different and appropriate teaching techniques for each age group while also providing information about the origins of particular styles of dancing to older students through interesting stories and discussion. \n \n Handling various administrative tasks, including parent communication, schedules, and billing. \n Achieving my MFA in Dance from Mills College and teaching an entry-level course titled “Introduction to Creative Dance” as a graduate assistant. \n Performing with the San Francisco Spark troupe for the past 13 years as a dancer, choreographer, producer, and media spokesperson (a full list of articles, references, and quotes available upon request). \n With my keen ability to develop and evolve new dancers, combined with my in-depth experience as a professional dancer, I am prepared to excel in providing excellent instruction at Chrysalis Dance Studio. I look forward to discussing the position, and my qualifications, in further detail. Thank you for your consideration. \n \n Sincerely, \n \n Martha Greenpots',
    editor=anna,
        liked_by=[anna, laura],
        rating=9)
    edited_ten = Edit(title='Cadburys New Recipe Feedback', original=writing_ten,
    text='I cant believe why my last few bars of chocolate tasted so different (threw some out). So, I looked online to see if others had experienced the same to find many negative reviews after a change in recipe. I\'m in my 60\'s and have used Cadbury\'s for most of this time. I\'m NOT impressed! I only have a few pieces with a cuppa for dessert... no more as will be buying another brand from now on after finding out that the actual recipe is different- not old nor spoilt chocolate',
    editor=anna,
        liked_by=[laura, ollie, alex,],
        rating=9)
    edited_eleven = Edit(title='Letter Concerning poor Service at Restaurant', original=writing_eleven,
    text='Dear Sir,\n visited your restaurant on 10 September 2013 for dinner with my family. We ordered Chinese food and requested the waiter for spring-rolls first. \n The starter came in after a long wait and turned out to be stale. Despite reporting the same to your supervisor, he denied our claim and was rude when he asked us to look for another restaurant instead. \n \nThe children started complaining of discomfort and we rushed them to a hospital wherein doctors declared food-poisoning. We could avert serious damages due to timely medical attention. \n \n I request you to kindly investigate and take action against the staff on duty for their negligence and rude behavior. I am sending a copy of hospital bills for reimbursement failing which I will take up the case to the Customers Forum for stringent action against your restaurant. \n \n Thanking You, \n \n Graham Short',
    editor=anna,
        liked_by=[laura, ollie, alex,],
        rating=9)
    edited_twelve = Edit(title='Letter providing coverage about web dev', original=writing_twelve,
    text='Use the article for information about this article and the best information for your information. If you like checking / XML / PLSL, look for product support? Send cable that requires product support. You can get a lot of products in the best place for new service languages ​​and you can get a character for it. Click here to see this article in this article for more information about your name or name targeting visually. We can post this article for your article in protecting your website. We can post this article for more information on this article. Click here to see this article in Germany. In the past five years, an exclusive article in the best place has the best position in the Internet language. Log in to your Account Manager. You can log in to your Account Manager. We can get this article on the web. Bracken Mist Hadden ',
    editor=laura,
        liked_by=[laura, ollie, alex,],
        rating=9)

    edited_thirteen = Edit(title='Vietnames/English Language Exchange', original=writing_fourteen,
    text='I want to meet someone to practice English with me, right now I only have a very basic level (I have had help to write this!) I can teach you Vietnamese in exchange! ',
    editor=laura,
        liked_by=[anna, lindsay, ollie, alex, harry, laura],
        rating=9)

    edited_fourteen = Edit(title='Nut Butter Start-Up Press Release', original=writing_fourteen,
    text='Leading Nut Butter and Confections Brand Launches Eleven Out-of-this-World New Products \n Wesley’s, maker of naturally delicious, high-quality nut butters, nut butter snacks and organic peanut butter cups, today announces 11 new SKUs of great tasting products to the brand’s extensive and admired nutty family. Officially being unveiled at this year’s Natural Products Expo West and rolling out on shelves over the course of the next few months, Wesley’s welcomes new firsts for the brand including a line of Cashew Butter and Dark Chocolate Almond and Cashew Butter Cups along with tasty line extensions in White Chocolate Mini’s, 28 oz. Peanut Butter and Cinnamon Almond Butter. \n \n “Calling all astro-nuts! I couldn’t be more excited to share my new nut butter-fueled products all blasting off at Expo West,” said Wesley Gold, founder of Wesley’s. “We’ve landed on not one, not two, but 11 fantastic new products that round out our nut butter and confections lines with new nut types, new flavors and new forms. The nut butter snacking possibilities are endless, and deliver the damn good taste and high-quality ingredients that consumers have come to love and expect from the brand. Wait until you taste our Maple Cashew—it’s giving Maple Almond Butter a run as my new personal favorite!”',
    editor=laura,
        liked_by=[anna, lindsay, ollie, alex, harry, laura],
        rating=9)

    edited_fifteen = Edit(title='Margaret Deedward\'s Obituary', original=writing_fifteen,
    text='Margaret, a long-time resident of the Hull area, died Wednesday the 18th of June at Sun Bridge Healthcare Center. \n \n Born in 1928 in Hull, S.D., Margaret received a Bachelor of Science in Nursing Education from South Hull State College in 1951. She continued her education at the University of Hull, from which she received her M.Ed. in Nursing in 1955. \n \n Margaret taught Nursing at the University of Hull at Amherst in the mid-1960s and worked at various psychiatric nursing facilities throughout western Massachusetts in the 1970s. In a career shift, she took a position as a librarian assistant at Hull County Technical School, where she worked until her retirement. \n \n Margaret loved good food and socializing, enjoyed going to movies and plays with friends, and had a wonderful smile that could light up a room. \n \n She is survived by her niece, Tabitha Winslow and several grandnieces, all of whom live in southern Hull, and brought great joy to her later years. \n \n Memorial gifts may be made to the Hull Valley Humane Society. \n The Douglass Funeral Service, Hull, has been entrusted with arrangements.', editor=laura,
        liked_by=[anna, lindsay, ollie, alex, harry, laura],
        rating=9)

    edited_sixteen = Edit(title='Press Release for Production of As You Like It', original=writing_sixteen, text='The Theatre People is pleased to present As You Like It against the backdrop of New York City during the Great Depression.  Shedding the opulence of the court for the Hooverville of Arden, Rosalind, Orlando and their co-mates explore the nuances of passion and classism in a pre-war setting.   Word play, music, and a couple of classic clowns make this one of Shakespeare’s best-loved comedies.', editor=laura)


    edited_seventeen = Edit(title='Letter of Apology', original=writing_seventeen,
    text='I feel I owe you a personal apology for my insensitive comment at the meeting yesterday. I know these days since John\'s funeral have been very difficult for you, and I was clearly out of order in making reference to "merry widows." I\'m sorry you had to suffer from my foolishness. \n \n I hope you will be able to forgive me. I have tremendous respect for you and your abilities, and I hope we can continue to work well together. I\'m terribly sorry.',
    editor=laura,
        liked_by=[anna, lindsay, ollie, alex, harry, laura],
        rating=15)

    edited_eighteen = Edit(title='The Game', original=writing_eighteen,
    text='The morning of June 27th was clear and sunny, with the fresh warmth of a full-summer day; the flowers were blossoming profusely and the grass was richly green. The people of the village began to gather in the square, between the post office and the bank, around ten o\'clock; in some towns there were so many people that the lottery took two days and had to be started on June 2th. but in this village, where there were only about three hundred people, the whole lottery took less than two hours, so it could begin at ten o\'clock in the morning and still be through in time to allow the villagers to get home for noon dinner. \n The children assembled first, of course. School was recently over for the summer, and the feeling of liberty sat uneasily on most of them; they tended to gather together quietly for a while before they broke into boisterous play. and their talk was still of the classroom and the teacher, of books and reprimands. Bobby Martin had already stuffed his pockets full of stones, and the other boys soon followed his example, selecting the smoothest and roundest stones; Bobby and Harry Jones and Dickie Delacroix-- the villagers pronounced this name "Dellacroy"--eventually made a great pile of stones in one corner of the square and guarded it against the raids of the other boys. The girls stood aside, talking among themselves, looking over their shoulders at rolled in the dust or clung to the hands of their older brothers sisters. Soon the men began to gather. surveying their own children, speaking of planting and rain, tractors and taxes. They stood together, away from the pile of stones in the corner, and their jokes were quiet and they smiled rather than laughed. The women, wearing faded house dresses and sweaters, came shortly after their menfolk.', editor=laura,
        liked_by=[anna, lindsay, ollie, alex, harry, laura],
        rating=15)

    edited_nineteen = Edit(title='Job Application Cover Leter', original=writing_sixteen, text='I noticed that my inbox (and embarrassing) holds 1500 unread messages, including at least 50 different type newsletters. But this only creates an email that is worth the opening. In my opinion, the use of your job is a real advantage. I\'ve been following Vitabe for a number of years, and I can say that I\'ll return any email you send me. I have a good cube for a good subject line - "Vitamin A is over - our favorite thing with ABC with my" favorite "- and how your email content feels fun and expert help, talking for the reason I I am glad to present your request to the email marketing email address of your company, I have four years of marketing experience, my current role at West Side Bank is to provide email designs. New data for new customers is analyzed and Analyze data on different types of customers that change with people who have already received money, as well as the results of the survey and tourism maps. We interacted, we were able to pay.% And 30% of these subscribers, as our result would be significantly higher than last year, I also focused on credit reports to educate my clients about How they manage and manage their records that have the highest record', editor=laura,
        liked_by=[laura, ollie, alex,],
        rating=15)

    edited_twenty = Edit(title='Harry Potter Fan Fiction', original=writing_twenty, text='Albus shifted under his blankets. He untangled his leg from his sheet (how did that happen?), and sat up in his bed as sunlight streamed through his window. He glanced down at Art, who was sleeping soundly in a sleeping bag on the floor. How was it that the person on the ground had the best sleep? Albus felt sweaty and uncomfortable. His neck ached slightly. He must have slept on it funny. Al got up and crept downstairs, to where Mum and James were eating breakfast. It was his ordinary, boring house- they had left Atlantis yesterday, after spending a day touring the city. \n \n “I presume Dad and Lily are still sleeping?” Albus asked, as he plopped down on a chair. \n \n “Actually, no. Lily’s still sleeping, but your father’s at work,” Al’s mum replied. \n \n “But I thought dad was coming with us to Diagon Alley today!” Albus said. That was the plan. They were going to spend two days at the World Cup, the day after that at Diagon Alley, and then Art was going back until school started. But dad was planning to be with them at Diagon Alley.\n \n “He was supposed to come with us, but at an unearthly hour this morning, your father was called into work. A few minutes later, I got a ten-second brief of what was going on.” \n \n “What did he tell you?” James asked eagerly. \n \n “Not telling. They don’t know much yet. As of this morning there was no hardcore evidence.” \n \n “Hardcore evidence of what?” James asked. \n \n “Come on mum, please?” Albus begged. Something that dragged his dad out on the morning of their Diagon Alley trip had to be exciting. \n \n “Sorry. You’ll probably see it in The Evening Prophet tonight anyway.” \n \n “Oooh, so it’s important enough for an edition The Evening Prophet?” James said excitedly. The Evening Prophet was only issued if there was exciting news that happened over the course of the day. \n \n “Possibly. If not, it will definitely be in the news tomorrow morning. Anyway, enough about that, you need to fill up on breakfast for our trip today.” \n \n Knowing that he would not be able to get anything else out of his mum, Albus asked, “We’re meeting Uncle Ron, Aunt Hermione, Rose, and Hugo at the Leaky Cauldron this morning, right?” \n \n “In about two hours, I believe.” Albus nodded. \n \n They ate in silence for the next few minutes. Albus gulped down a large glass of orange juice, and resumed eating his toast.', editor=laura,
        liked_by=[laura, ollie, alex,],
        rating=15)

    edited_one_two = Edit(title='This Poem Is Intended For Yourself', original=writing_one,
    text='I am envious of the small pieces of rock\n under yourself \n surrounding yourself \n what you purvey \n sparkling elements \n  rubbed out woman \n shining and going without copious quanitites of baggage \n viscous material \n before the thing that marks the spot \n your name is written in biro upon my shoulder blade \n musicality \n perishes downwards \n I too grew up in \n the soft finger plates \n of the deities \n and small equine mammal \n Tears, tears, and I am aware \n just what they seem to signify \n flowers not in the day \n  I have done this poem FOR YOURSELF and haven\'t mislaid it (yet)',
    editor=laura,
        liked_by=[anna, lindsay, ollie, alex, harry, laura],
        rating=15)
    edited_two_two = Edit(title='Complaining To British Airways', original=writing_two,
    text='To whom it may concern, I write to say bad things from two trips from Cape Town to London Heathrow on 19/04/19. As you know, the entertainment did not succeed on board the entire flight for 11 hours. Our crew was rude and unhelpful throughout the trip, making it a very unpleasant experience. The hotel is located in the north section of BA 20 LE per coupon. \n \n After riding the place directly, we noticed that the onboard entertainment system was not working. We did not take off yet, but the cabin crew told us that it was possible to reset the system after Greg Underwood, the customer relations manager, told her that the system was not working. After three 45 attempts and about 45 minutes without updating, I heard many other passengers asking the cabin crew what to do. They were met with the frustration, frustration and defensive attitude of our cabin vampires - specifically Matilda and Philip. I heard Matilda telling the inquiring passenger that the situation was "unfair" to the staff and she moved away without apologizing. Each of the crew members ignored the case for more than two hours and we have not received any apology yet. At the end, Greg spoke to each of the affected passengers and apologized for the problem. I told her that we felt as if the cabin crew had ignored the situation and that much could have been done to apologize. We received a complaints bulletin and informed us that we would receive compensation. \n \n nI would like to take this opportunity here to add that while she was talking to a rear passenger, who spent the previous 11 BA flight with broken screens, Greg admitted that the plane was "very old" and that the screens were "broken all the time". I am shocked and shocked that a company with a reputation for British Airways will deliberately allow passengers to spend their money on seats that do not have the basic amenities we pay for. In addition to the broken screens during the 11-hour journey, the cabin crew was rude and unhappy to return to the flight, picked up passengers and did not help meet our basic requests, such as drinks. At the end of the trip, Matilda was pouring coffee for travelers. However, a few rows were stopped in front of us and no Deedwarder. Later, Philip returned with tea. The passengers behind the coffee asked politely, and Phillip replied, "I did not make an offer to get more or apologize for the crew\'s mistake." In addition, during the flight, I heard another passenger very upset about not eating It was a terrible experience from start to finish and definitely required a large amount of £ 20 for compensation. My Yoni Yoni Ya Yoni Ya Yoni Ya Yoni Y Me',
    editor=harry,
        liked_by=[anna, lindsay, ollie, alex, harry, laura],
        rating=15)
    edited_three_two = Edit(title='Applying to Become A Master of Alcolic Beverages, sutuated behind a Bar', original=writing_three,
    text='Miss Appleby: After reading about your need to be a new member, you can join me. In addition to providing excellent clients with casual and classy dining experiences, having a good knowledge of team collaboration and leadership, I greatly benefit from this role at McIntyre Bar and Grill. General Discussion \n My experience in preparing and transporting cocktails, beer, wine and spirits to different clients has prepared for this role. My ability to achieve this capability is government preparation, inventory management, and managing people. I can produce faulty alcohol while maintaining a clean and safe environment, and have the ability to interact and communicate and manage time. Examples of my background are: The Hygiene Line takes customers and orders, delivers the right food and drink, collects and makes money, maintains excellent inventory levels, and quickly. It also balances several restaurant functions. enables managers to create a full range of operational tasks and provide better customer satisfaction support. \n Demonstrate team building and planning skills, strong leadership skills and unique interpersonal skills, tips for new employees in regular bar and restaurant operations. If my past experience and enthusiasm and ability, and the neutrality of New York, I would like to highlight my expectations for this role. I look forward to discussing this post in more detail. Thanks for looking. \n Unfortunately, Horsehead',
    editor=harry,
        liked_by=[laura, ollie, alex,],
        rating=15)
    edited_four_two = Edit(title='Gratitude is the apt response in this circumstance (wedding attendance)', original=writing_four,
    text='We thank you sincerely for celebrating your day with you and making it the most memorable day of your life. During the ceremony, I danced all day in the rain, sliding together, you felt the day of love. We can\'t wait to travel to Europe at the end of July, this can\'t happen without all your good gifts. \n We look forward to starting the next chapter of our lives and sharing more memories with you! "',
    editor=harry,
        liked_by=[anna, lindsay, ollie, alex, harry, laura],
        rating=14)
    edited_five_two = Edit(title='Be My Valentine', original=writing_fourteen,
    text='If you were a fool, I was in the sun and when it rained I fell on the ground. I will change the tour late at night so that I can keep it in good light. If you are in my world I will be the light of the night in your moon, quiet boundary, darkness. Together, our two groups sometimes move our dance to dance. If you are on my island, I will be on your shore and clean the ocean softly and gently. This series assumes sandy beaches, but now with thunderstorms, I like soft scenery. If you promised to love, if the stars are not right I\'ll be in time. And we are people, but absolutely love is in love, and it will be my eternal loyalty to Valentine.',
    editor=harry,
        liked_by=[anna, lindsay, ollie, alex, harry, laura],
        rating=13)
    edited_six_two = Edit(title='Letter to Become PA', original=writing_six,
    text='Dear Felix, I represent my agent, I am happy with your work and I believe in your experience and skills so that I can fill you as a candidate. When you advertise your service, it shows that the company\'s CEO needs his own experience to support all aspects of the project. My current role as a direct assistant. I act as a key gateway between him and his team to ensure that he can focus on actions that reduce his chances of personal attention and reduce his decision. To continue here, I see how to be successful with others. Wechsler courses are 7%. In addition, I use my communication and communication skills to edit meetings, meetings, and rockets. This belt gave me the protocol for such meetings because of my ability to intrude on swallowing. Listen, thanks for reviewing your request, so Elena Biszorp',
    editor=harry,
        liked_by=[anna, lindsay, ollie, alex, harry, laura],
        rating=13)
    edited_seven_two = Edit(title='My Brand', original=writing_fourteen,
    text='A focused and purposeful business leader, I propose entrepreneurial persistence and wisdom to stimulate profit growth and profitable business, inspire employees to achieve maximum productivity and develop profitable business relationships based on respect, loyalty and trust. My calm sense of humor was the defining management strategy to bring out the best in everyone, instill pride and mobilize them to make their company the best in the industry.',
    editor=harry,
        liked_by=[lindsay, ollie, alex, harry],
        rating=13)
    edited_eight_two = Edit(title='Restaurant Complaint', original=writing_eight,
    text='My wife and her wife, I recently visited a mysterious meat restaurant at 341 Hampton Rd. Friday, June 6. We arrived around 11:45. I\'ve added a copy of my invoice for your convenience. This is a place close to our office. We met there at least five times last year. Our experience on Friday is not positive. We are not happy with the purity and the sense of what you need to know. All deserted tables are dirty and full of rubbish and rubbish. In addition, the floor clean the house. The bathroom is not very clean. In the past, the restaurant was clean. We really enjoy having Happy Taco. If improvements are made, we are more likely to meet in the future. Usually we visit at least once a month. Contact me. Thank you for your feedback. Good day to you And frankly, William McPurry',
    editor=harry,
        liked_by=[lindsay, ollie, alex, harry],
        rating=13)
    edited_nine_two = Edit(title='I will be an excellent instructor of dance!', original=writing_nine,
    text='My inspiration for teaching dance comes from the same influence that led me to my dance career nearly 13 years ago. Since the beginning of my education in the art of play, I have been trying to use body language to tell stories and emotions in new languages, and I have been a strong supporter of teaching others. Throughout my career, I have seen dance as a way to enrich the life of dance and theater, and as my dance teacher, I see students learning different types of dance and following their creative expression. Believe in motivation. I think dance is an early experience in shaping the perspectives of people, interested in developing their own experiences of creativity, creativity, and beliefs. \n \n Reviews of my experience include ... \n \n A group group 4 to 14 years ago as a young dancer as Berkeley Dance Studio coach; performs dances and activities, keeping students busy and happy. Introduce tips, observations, and art and music for students to observe. \n \n While providing information on adult dance style through interesting stories and discussions using a variety of teaching techniques for each group. \n \n Manage various administrative tasks, including parent communication, schedules and payments.  I am getting my MFA in Dance at MFA College and an introductory level course in natural dance as a graduate assistant. San Francisco Spark Temp has worked for the past 13 years as an illustrator, artist, journalist, and speaker (a full list of articles, testimonials, and art available on request). \n With my deep experience as a professional dancer and inspiring a new dancer and changing my skills, I have succeeded in providing Chrysalis Dance Studio. I look forward to discussing my position, and my qualifications further. Thanks for your attention. \n \n Sincerely, \n \n Martha Green Potts',
    editor=harry,
        liked_by=[lindsay, ollie, alex, harry],
        rating=13)
    edited_ten_two = Edit(title='Cadbury\'s Complaint', original=writing_ten,
    text='I do not want to believe that the last chocolate bar has a different taste, so it\'s different. So I look at the web to see that others experience the same as getting many negative reviews after changing the formula. I\'m 60 years old and have used most Cadbury. I\'m not interested! I just have a couple of pieces for a cup of tea ... I will not buy another brand from now on finding the exact formula does not differ from the other and does not break with the chocolate ',
    editor=harry,
        liked_by=[anna, lindsay, ollie, alex, harry, laura],
        rating=13)
    edited_eleven_two = Edit(title='Restaurant Complaint', original=writing_eleven,
    text='Dear Sir, I went to your restaurant on September 10, 2013 for dinner with your family. We ordered the Chinese food and asked the waiter for the spring rolls first. wait n The opener became obsolete after a long wait. He reported it to his supervisor, but he declined our comment and was horrified when he asked us to find another restaurant. \n \n The children started complaining about the discomfort and we took them to a hospital. Doctors declared food poisoning. Timely medical care can prevent serious harm. \n \n I urge you to kindly investigate your negligence and indecent behavior and take action against the service officers. I will send a copy of the hospital bill for a refund to take the case to the Consumer Forum to take strict action against your restaurant. \n \n Thanks, \n \n Graham Short',
    editor=alex,
        liked_by=[anna, lindsay, ollie, alex, harry, laura],
        rating=11)
    edited_twelve_two = Edit(title='Web Dev Cover Letter', original=writing_twelve,
    text=' Mr. Martina, N I recently read my latest release on Junior Web Developer. Focusing and focusing on detailed information and common understanding of HTML and Java / XML / PLSL is a special option. As a current entrepreneurship, I am certified and fully distributed according to the applications, fully design. Depending on the wording and the effectiveness of the advertising programs, we still add great code to the broadcaster\'s form. With all my caution and hard work, I have received general promotions and bonuses. I hold a Bachelor\'s degree in Information Technology and General Information and Certification. Can write great laws, speak clearly and work with partners. I\'m a 5 year old company specializing in business and I want to provide information about specialized companies. In all competencies, she is the exclusive representative of the Junior Web Developer position. Call to arrange an interview. I follow my body and look forward to the meeting. Against Brackensmist Hadden',
    editor=alex,
        liked_by=[lindsay, ollie, alex, harry],
        rating=11)


    edited_thirteen_two = Edit(title='Start-Up Press Release', original=writing_thirteen,
    text='I want to meet someone to practice English with me, right now I have only a very basic level (I have help to write this article!) I can teach you Vietnamese to exchange!',
    editor=alex,
        liked_by=[anna, lindsay, ollie, alex, harry, laura],
        rating=11)
    edited_fourteen_two = Edit(title='New Nut Butter Brand Is Answer To Your Nutty Prayers!', original=writing_fourteen,
    text='"Walnut and named confectionery produce eleven new products out of the world. Natural Delley Wesley, Walnut Fuel Diet, Coconut Oil and Grilled Glasses, are now 11 brand new, to choose a wide range of products after branded, it was officially released at the West Products Expo 2012, and will feature new discoveries over the coming months, including Almond Oil Cashew and Almond Cashew Oil, and Delicious White Extensions Chocolate Mini at 28 Walnut Oil. Call all nuts! Wesley Gold, co-founder of Wesley Gold, said: "I\'m very excited to introduce Walnut Oil Brass Products at Expo West." "We have given 11 new products, not just one, but also two new varieties of nuts, new flavors and new forms that differentiate between walnuts and sugar. Wait until you have a Maple Cashew taste. bones like my new favorite character! "', editor=lindsay)

    edited_fifteen_two = Edit(title='RIP Maggie', original=writing_fifteen,
    text='Margaret, who has lived in the Hole community for a long time, died Wednesday, September 18, at the Sun Bridge Health Center. Ann In 1928 Hull, SD, Margaret received her Bachelor of Science in Nursing from Hull University Lace School in 1991. He resumed his education at Hull University, where he attended. Get your MD in Nursing in 1955. Margaret taught at Hull University in Amsterdam in the mid-1960s and worked in nursing homes throughout Massachusetts in the 1970s. He took a post as librarian at Hull County Technical School, where he worked until his retirement. Margaret loves good food and flowers, enjoys movies and games with friends, and has a big smile that can brighten a room. His father-in-law, Tablia Winslow and many of his grandparents, all living south of Hull, have been very happy in the years to come. Memorial gifts may be made to the human society of the Humpty Hole. Douglas, Hull\'s service was established.', editor=lindsay)

    edited_sixteen_two = Edit(title='We Think You WILL Like It!', original=writing_sixteen, text='The theater people are pleased to announce Your Love Against the Background of New York City during the Great Depression. Conducting court-appointed opulence presentations for Hooverville of Arden, Rosalind, Orlando and their colleagues navigated estimates of love and class conditions in a military setting. Working words, music, and a pair of classic comics make it one of Shakespeares favorite comics.', editor=lindsay,
        liked_by=[anna, lindsay, ollie, alex, harry, laura],
        rating=11)

    edited_seventeen_two = Edit(title='Letter of Apology', original=writing_seventeen,
    text='I feel you have a personal apology for the meeting yesterday. I know these days because I\'m sorry. I will be able to forgive me. I have great work honors together. I\'m very sorry.',
    editor=laura,
        liked_by=[anna, lindsay, ollie, alex, harry, laura],
        rating=11)

    edited_eighteen_two = Edit(title='Short Story About Stuff', original=writing_eighteen,
    text='On the morning of June 27, it was clear and sunny, with the warmth of the whole summer; The flowers blossomed and the grass was green. Rural people began to gather about ten hours on the square between the post office and the bank; Many people in the city took the lottery for two days starting June 2. Only about three hundred people lived in the village, and the lottery took less than two hours, so it started at ten o\'clock in the morning and the villagers needed time to have dinner at home. After all, the boys met. The school was recently summer, and they often surrounded themselves with a sense of freedom, and gradually they quietly assembled for a while before the start of the game. And their speech was from the class and the teacher, books, and reprimands. Bobby Martin poured stones into his pockets, and the other boys chose the softest and roundest stones soon and followed his example; Bobby and Harry Jones and Dickey Delacroroy - the people of the village called the Dellacroi - eventually made a big pile in one corner of the square and protected the other children from aggression. The girls differed from each other, talked, looked at their shoulders, turned dust, or clung to their elder brothers. Soon people gathered. Talk about their children\'s survival, sowing and rains, tractors and taxes. They stood far away from the stones gathered around the corner, and instead of laughing, they were silent and smiling. Women wearing stale home dresses and sweatshirts came shortly after their own people.', editor=laura,
        liked_by=[anna, lindsay, ollie, alex, harry, laura],
        rating=11)

    edited_nineteen_two = Edit(title='Cover Letter', original=writing_nineteen, text='I have a problem. See, my inbox currently (and embarrassingly) hosts 1,500 unread emails—including newsletters from at least 50 different brands. \n But this problem only fuels my passion for creating emails that are worth opening. Because from my perspective, as someone who can barely get through their own stack of mail, that’s a true win. \n \n I’ve been following Vitabe for years, and can proudly say that I open every single email you send to me. I’m a sucker for a good subject line—“Take a Vitamin-ute—We’ll A-B-C You Soon” being my favorite—and the way your email content feels both fun and expert-backed really speaks to me. This is why I’m thrilled to submit my application for a role as email marketing manager at your company. \n \n I have over four years of experience working in the email marketing space. In my current role at Westside Bank, I was able to implement new email campaigns centered around reengaging churned clients. By analyzing data around the types of clients who churn and the engagement of our current email subscribers, as well as A/B testing headlines and newsletter layouts, we were able to increase email subscribers by 15% and convert 30% of those subscribers to purchase our product, a significant increase from the previous year. I also launched a “Your Credit Matters” newsletter focused on educating our clients on how they spend and manage their credit—which became our highest performing campaign in terms of open-rates and click-through to date.', editor=laura,
        liked_by=[anna, lindsay, ollie, alex, harry, laura],
        rating=11)

    edited_twenty_two = Edit(title='HP FF', original=writing_twenty, text='Albus moved under his blankets. His leg was torn off his plate (how did this happen?), And he sat in his bed, so that sunlight flowed through his window. She looked at art, who slept slowly in a sleeping bag on the floor. How did the person get the best sleep on earth? Albus felt sweaty and sad. His neck bent slightly. He must have laughed at her. Al up and down stairs, where mom and James ate breakfast. Her usual home is boring - she left yesterday Atlantis, after a day trip around the city. "I think Father and Lily are still sleeping?" Albus asked: He is tied up in the chair.  "Indeed, neither is Lily still asleep, but your father at work, the mother answered." But I thought Dad with us came to Diagon\'s Alley today! "It\'s their program they have two days in the World Cup, the next day It started on Diagon alley, and then art to school, but your father wanted to go with them on the Diagon , which was supposed to fall with us, but at an hour after this second morning, your father "What happened to you?" "What did he say to you?" James asked enthusiastically: "We do not say that they still do not know much. There was no strong evidence from this morning.""A strong certificate From what? " James asked, "Come on, mother, please?" Albus asked what was exciting to drag her father in the morning of her Diagon alley trip. Probably you will see the evening prophet tonight tonight. Oh, so, enough for the Prophet\'s version of the important era? "It\'s possible that the exciting news that was published during the day that the Prophet Muhammad was published the next morning," James excited. If not, surely it will be on the morning of the day. So you have to fill your breakfast today. Aunt Hermione, Rose, and Hugo in the liquid kettle this morning, right? about two hours, I think." Albus noted, they ate slowly for a few minutes. Albus left a glass of orange juice and wasted away from eating his own bread.', editor=laura,
        liked_by=[anna, lindsay, ollie, alex, harry, laura],
        rating=18)


    edited_one_three  = Edit(title='For You', original=writing_one,
    text='I envy the small parts of the rock that surrounds you \n N around you \n what you offer \n" glittering elements \n "of women \n n without large quantities of luggage \n adhesives \n n before the thing that represents the place.I grew up on the soft fingers of the gods and small mammals Tears and tears, I realized what flowers seem to be not today means that \n NI have manufactured this poem by HIMSELF and have not lost it (yet)',
    editor=alex,
        liked_by=[anna, lindsay, ollie, alex, harry, laura],
        rating=18)
    edited_two_three = Edit(title='Making A Very Excellent Formal Complaint to BA', original=writing_two,
    text='Who is to be touched by this, I wrote to some on April 19, 1919, after a two-way trip from Cape Town to London Heathrow. As you know, on-board entertainment completely fails in 11 hours. Our staff was stubborn and extremely compelling during the trip, which made it very unpopular. The hotel is north of BA 20 LE per vote. After a live performance, we found out that the entertainment system on the board didn\'t work. We did not start, but the cockpit staff told us that it was possible to restart the system after Greg Underview, a customer communications manager, told them that the system was not working. After trying for three to 45 minutes without restoration, I heard what a lot of passengers should do with this crew. They have experienced vampire confusion, frustration and self-defense in our wardrobe, especially in Medellia and Philip. I heard informing passengers that the situation was described as "unfair" and that they left without apology. Each staff member left the case for more than two hours and was never found. Finally, Greg spoke to each of the affected passengers and apologized for the problem. I told her we felt the staff situation was rejected and that they were probably apologizing. We received a complaint message and were told that we would receive compensation. I would like to say that while talking to the passenger on the occasion, who was on BA\'s 11th flight with a broken screen, it was admitted that the aircraft was "very old" and the screen was "everywhere", When it was astonished that the British Airways Company had deliberately allowed passengers to use it. Their money is on seats that were not available. We provide basic facilities. In addition to the broken screen during the 11-hour flight, the staff was stubborn and unhappy when they returned to the ship, picking up passengers and forcing us to meet basic needs, such as alcohol. General Chat Chat Lounge At the end of the trip, Matilda served guests quite a bit. However, some lines were closed in front of us and they were gone. Then Philip brought some tea. The passengers were quite comfortable, and Philip replied, "I made no suggestions to find the staff\'s fault or to apologize." Also, during the flight, I heard another sad passenger about food. It was a bad experience from start to finish and £ 20 on a large scale is needed to pay for them.',
    editor=anna,
        liked_by=[lindsay, ollie, alex, harry],
        rating=18)
    edited_three_three  = Edit(title='Bar Job Cover Letter', original=writing_three,
    text='Dear Ms. Applebee: \n When I learned of your need for a new member to join your bar staff team, I hasted to send you my resume for your consideration. With key experience providing excellent customer service in both casual and fine dining establishments—as well as my commitment to dynamic team collaboration and leadership—I would significantly benefit McIntyre Bar & Grill in this role. \n My experience in preparing and delivering cocktails, beer, wine, and spirits for diverse clientele has prepared me to excel in this role. Complementing this expertise is my proficiency in order taking, table setting, stock management, and premises maintenance. With my proven ability to create sophisticated alcoholic and non-alcoholic beverages while maintaining a clean and safe environment, my additional strengths in communication and time management position me to thrive in this position. \n \n Highlights of my background include: \n \n Greeting bar guests and taking orders, delivering accurate food and beverage items, collecting and processing payments, maintaining optimal inventory levels, and balancing multiple tasks simultaneously in fast-paced restaurants. \n Providing overarching support to bar managers with a full range of operational tasks to achieve top levels of efficiency and customer satisfaction. \n Demonstrating team building and organizational planning abilities, strong leadership talents, and exceptional interpersonal skills; mentoring new staff in general bar and restaurant operations. \n With my previous experience, coupled with my enthusiasm and my personable, outgoing demeanor, I could swiftly surpass your expectations for this role. I look forward to discussing the position in further detail. Thank you for your consideration. \n \n Sincerely, \n \n Hamish Horesdale',
    editor=alex,
        liked_by=[lindsay, ollie, alex, harry],
        rating=10)
    edited_four_three = Edit(title='Thanks for coming to our big day, loved the money!', original=writing_four,
    text='We are so so so so so full of thank you for celebrating our massive twenty four hours in combination with us, which made it one of the most memorable days in your life. During the event, I danced all day in the rain, jumped together and felt the day of love. We can not wait to go to Europe at the end of July, it will not happen without all the good gifts. We look forward to the next chapter of our life and share with you new memories! "',
    editor=harry,
        liked_by=[lindsay, ollie, alex, harry],
        rating=10)
    edited_five_three  = Edit(title='Valentine', original=writing_five,
    text='If you were my rose, then I\'d be your sun, \n painting you rainbows when the rains come. \n I\'d change my orbit to banish the night, \n as to keep you in my nurturing light. \n \n If you were my world, then I\'d be your moon, \n your silent protector, a night-light in the gloom. \n Our fates intertwined, two bodies in motion \n through time and space, our dance of devotion. \n \n If you were my island, then I\'d be your sea, \n caressing your shores, soft and gentle I\'d be. My tidal embrace would leave gifts on your sands, \n but by current and storm, I\'d ward your gentle lands. \n \n If you were love\'s promise, then I would be time, \n your constant companion till stars align. \n And though we are mere mortals, true love is divine, \n and my devotion eternal, to my one valentine. ',
    editor=harry,
        liked_by=[lindsay, ollie, alex, harry],
        rating=9)
    edited_six_three  = Edit(title='Hire Me and I will assist YOU!', original=writing_six,
    text='Dear Felix, On behalf of my representative, I love your work and I believe in your skills and abilities to help you finish it. When a service is issued, the President of the company expresses his need to assist him in both aspects of the project. My current role as auxiliary support. I am a key player between my team and team so that I can focus on minimizing activities my chance to reduce self and reduce my choices. To continue this activity, you will learn to benefit others. Wechsler 7% class. It also uses direct connection with meetings, meetings, and preparation of papa. This file is recommended for advisory plans when discouraged. Thank you for reviewing your application. This is Elena Biszorp',
    editor=harry,
        liked_by=[lindsay, ollie],
        rating=9)
    edited_seven_three = Edit(title='Personal Brand Statement', original=writing_seven,
    text='A focused and determined business leader, I offer the entrepreneurial stamina and wisdom to drive bottom line growth and lucrative business, inspire employees to peak performance, and cultivate profitable business relationships built on respect, loyalty, and trust. My easy-going sense of humor has been a defining management strategy to bring out the best in everyone, instill pride, and mobilize them to make their company the best in the industry.',
    editor=lindsay)
    edited_eight_three = Edit(title='Fast Food Complain', original=writing_eight,
    text='I visited an anonymous restaurant at 341 Hampton Rd. Friday, June 6. We arrived at 11.45. Please provide me with a copy of the invoice for your convenience. This is the nearest office. We met at least five times last year. Our Friday experience was a no brainer. We are not satisfied with chastity and curiosity. All the garbage tables are dirty and full of junk and junk. In addition, the house cleans the floor. The bathroom is not very clean. Previously, the restaurant was clean. We enjoyed Taco\'s joy. If improvements are made, we may meet in the future. We usually visit at least once a month. Hide me. Thanks for the answer. Hi to you, William McPurry',
    editor=lindsay,
        liked_by=[lindsay, ollie],
        rating=9)
    edited_nine_three = Edit(title='Dance Teach CL', original=writing_nine,
    text='My inspiration for dance lessons came from the same effect that led me to my dance career nearly 13 years ago." Since the onset of my education in the arts, I have tried to use the language of the body to tell stories And feeling in the new language, and I became a strong supporter of teaching others. Throughout my career, I have seen dancing One to increase the life of dance and drama, and as my dad, I see students learn different kinds of dance and follow their creative expression, believe in encouragement. Dancing is the first experience to develop the perspective of people who are interested in creating their own experience of creative, creative and creative. Believe me. Attempting my experience is related to ... A group of dancers aged 4 to 14 years old as a young dancer, Beck Cred studio studio. Dance and activities make the students happy and happy. Introduce tips, music and music for students to experience.  In giving information about the dance style Adults with a fascinating story and discussion by using various teaching methods for each group. Manage different administrative tasks, including parental, scheduling, and payment communications. I got my MFA to dance at the MFA College and an introductory level in Natural Dance as a graduate assistant. San Francisco Spark Temp has been working for 13 years as a painter, artist, journalist and guest speaker (for a complete list of testimonials and art available upon request). My deep experience as a professional dancer and to inspire new and varied singers, I have successfully delivered Chrysalis Dance. I look forward to discussing my position and my advantages. Thanks for your attention. \n \n Sincerely, \n  nMartha Green Park',
    editor=harry,
        liked_by=[lindsay, ollie],
        rating=9)
    edited_ten_three = Edit(title='No, Cadbury\'s No.', original=writing_ten,
    text='"I do not want to believe that the last chocolate bar has a different taste, so it\'s different, so I look online to see how other people have had a lot of negative analyzes after changing the same formula. Years and have used Cadbury, I\'m not interested! I have a little pie for a cup ... I will not buy another brand from now on to find D The correct formula is no different, and it does not break with the dark chocolate.',
    editor=harry,
        liked_by=[lindsay, ollie],
        rating=9)
    edited_eleven_three = Edit(title='Complaint to Restaurant', original=writing_eleven,
    text='Dear Sir, I went to your restaurant on September 10, 2013 for dinner with your family.  He reported it to his supervisor, but he declined our comment and was horrified when he asked us to find another restaurant. \n \n The children started complaining about the discomfort and we took them to a hospital. Doctors declared food poisoning. Timely medical care can prevent serious harm. \n \n I urge you to take action against the service officers. I will send a copy of the hospital bill for a refund to take the case to the Consumer Forum to take strict action against your restaurant. \n \n Thanks, \n \n Graham Short',
    editor=lindsay,
        liked_by=[lindsay, ollie],
        rating=6)
    edited_twelve_three  = Edit(title='Junior Web Developer Cover Letter', original=writing_twelve,
    text='Dear Mr. Martinez, \n \n I read with enthusiasm your recent advertisement for the Junior Web Developer position and am writing to express my interest. My superior focus and attention to detail combined with my extensive knowledge of HTML Javascript XML and SQL/PLSQL makes me an exceptional choice. \n \n In my current role as a Junior Web Developer I have developed web-based applications from design to coding and full implementation under the direction of the Senior Developer. By relying on solid programming knowledge as well as excellent oral and verbal communication I have consistently produced terrific code within customer-set deliverables time frames. Due to my diligence and hard work I have been awarded regular promotions and bonuses as a result. I bring a Bachelor’s Degree in Information Technology along with regular updates and certifications. My abilities to produce excellent code and to clearly communicate and collaborate with coworkers customers and management have led to company successes. I have five years of Junior Web Developer experience and am committed to staying up-to-date with all technological advancements. All of my qualifications make me an exceptional candidate for the Junior Web Developer position. \n \n Please call to schedule an interview. I have enclosed my resume and look forward to meeting. \n \n  Sincerely, \n \n Fiona Brackensmist Hadden',
    editor=anna,
        liked_by=[lindsay, ollie],
        rating=6)


    edited_thirteen_three  = Edit(title='Start-Up Press Release', original=writing_fourteen,
    text='I want to meet someone to practice English with me, right now I have a very good experience!',
    editor=anna,
        liked_by=[lindsay, ollie],
        rating=5)

    edited_fourteen_three  = Edit(title='GO NUTS FOR NUTS (in the form of butter)!', original=writing_fourteen,
    text='Named Nuts and Confectionery producing eleven new products from around the world, Natural Delley Wesley, Walnut Fuel Diet, Coconut Oil and Grilled Glasses, are 11 new to choose from. a wide range of branded products, has been officially launched at the West Products Expo 2012 and will feature new discoveries in the coming months, including almond cashew and cashew oil and the tiny white chocolate Delicious Extension 28 Nut Oil Call All Nuts Wesley Gold, co-founder of Wesley Gold, said: "I am very excited to introduce Walnut Oil Brass Products at the West Expo." "We\'ve given 11 new products, not just one, but also two new nut varieties, new flavors, and new shapes that distinguish between nuts and sugar. Wait until you get a Maphe Cashew flavor. Bones as my new favorite character!"', editor=lindsay,
        liked_by=[anna, lindsay, ollie, alex, harry, laura],
        rating=10)

    edited_fifteen_three  = Edit(title='May Margaret Rest In peaceful Slumber', original=writing_fifteen,
    text='Ms Margaret, who has lived in the Hull community for a long time, passed away on Wednesday, January 18 at the Sun Bridge Health Center. In 1928 Hull, SD, Margaret accepted her Bachelor of Science in Nursing from Hull University High School in 1991. He resumed his education at Hull University, where he attended. Get your MD in Nursing in 1955. Margaret taught at Hull University in Amsterdam in the mid-1960s and worked in nursing homes in Massachusetts in the 1970s. He took a post as librarian at Hull County Technical School, where he worked until his retirement. Margaret loves good food and flowers, enjoys movies and games with friends, and has a big smile that can shine in a room. Her in-laws, Tablia Winslow and many of her grandparents, all living south of Hull, are delighted in the years to come. Memories can be gifted in human society at the Empty Hole. Douglas service, Hole was established.', editor=lindsay,
        liked_by=[lindsay],
        rating=1)

    edited_sixteen_three  = Edit(title='We Think You WILL Like It!', original=writing_sixteen, text='The theater people are proud to announce Your Love Against the Background of New York City during the Great Depression. He held court-appointed discontent presentations for Hooverville from Arden, Rosalind, Orlando and their colleagues steering estimates of love and class conditions in a military location. Working words, music, and a pair of classical comics make it one of Shakespeare\'s favourite comics', editor=lindsay,
        liked_by=[lindsay],
        rating=1)

    edited_seventeen_three = Edit(title='Letter of Apology', original=writing_seventeen,
    text='I feel you really really deserve a MASSIVE MASSIVE SORRY! A personal proper apology for the meeting yesterday. I know these days because I\'m sorry. I hope you will be able to forgive me. I have great work honor to work together with you. I\'m very sorry. Please please forgive me.... ',
    editor=laura,
        liked_by=[lindsay, laura, anna],
        rating=7)

    edited_eighteen_three = Edit(title='Story SHORt', original=writing_eighteen,
    text='On the morning of June 27, the heat was clear all summer. Too much piece and green grass. The man stopped for ten minutes at the post office and the bank. Many people started working in the city on June 2 for two days. There were only three hundred people living in rural areas and the crisis went down for two hours, so that the morning started at ten and the villagers needed food. After the chat boy. It was a summer school and often surrounded his independence and quickly started working. And lectures on class and teacher, books and titles. Bobby Martin picked up his stones and quickly and easily received other children to get the most beautiful and bright stones. Bobby and Harry Jones and Dickie Dellcrovey - people in the village say - have finally been built in forest areas and other children protected by the ceasefire. Boys are different, talking, looking at their stones, stealing or becoming strangers to their ancestors. Talk about kids, forests and mountains, tractors and tax collection early. They stood around the rock, gathered around the boat, replaced instead, were quiet and quiet. Women\'s clothing and bedding are near their time.', editor=laura,
        liked_by=[lindsay, laura, anna],
        rating=7)

    edited_nineteen_three = Edit(title='Letter of Cover', original=writing_sixteen, text='I have difficulty seeing that my inbox (and embarrassment) keeps 1,500 emails unread - including newsletters from at least 50 different species. n But this problem just makes me create emails worth the opening. From my point of view, using his job is a real benefit.  I\'ve been following Vitabe for many years and I can say that I will open any email you send to me. I have a nice cube for a good subject line - "Check out vitamin-ute - our favorite thing comes from ABC" is my favorite - and how your email content feels fun and specialist support, talking to me. For this reason, I am pleased to present my application for the position of marketing manager for email in your company. I have four years of experience in email marketing. My current role at West Side Bank was possible to run new email initiatives that were enforced on customers. By analyzing data on the different types of customers that are changing and interacting with the people currently receiving money, in addition to the A / B exam results and the touring drawings. letters, we managed to charge the fees by 15% and 30% of these subscribers In order to buy our result, a significant increase from the previous year. I also focused on the Credit Matters newsletter to educate our customers on how they spend and manage their credit, which is the highest level of open recordings which they hold. clicks.', editor=laura,
        liked_by=[lindsay, laura, anna],
        rating=7)

    edited_twenty_three = Edit(title='Album Dumble-More', original=writing_twenty, text='Albus moved under his blankets. His leg was torn off his plate (how did this happen?), And he sat in his bed, so that sunlight flowed through his window. She looked at art, who slept slowly in a sleeping bag on the floor. How did the person get the best sleep on earth? Albus felt sweaty and sad. His neck bent slightly. He must have laughed at her. Al up and down stairs, where mom and James ate breakfast. Her usual home is boring - she left yesterday Atlantis, after a day trip around the city. "I think Father and Lily are still sleeping?" Albus asked: He is tied up in the chair.  "Indeed, neither is Lily still asleep, but your father at work, the mother answered." But I thought Dad with us came to Diagon\'s Alley today! "It\'s their program they have two days in the World Cup, the next day It started on Diagon alley, and then art to school, but your Dad wanted to go with them on the Diagon , which was supposed to fall with us, but at an hour after this second morning, your father "What happened to you?" "What did he say to you?" James asked enthusiastically: "We do not say that they still do not know much. There was no strong evidence from this morning.""A strong certificate From what? " James asked, "Come on, mother, please?" Albus asked what was exciting to drag her father in the morning of her Diagon alley trip. Probably you will see the evening prophet tonight tonight. Oh, so, enough for the Prophet\'s version of the important era? "It\'s possible that the exciting news that was published during the day that the Prophet Muhammad was published the next morning," James excited. Otherwise, surely it will be on the morning of the day. So you have to fill your breakfast today. Aunt Hermione, Rose, and Hugo in the liquid kettle this morning, right? about two hours, I think." Albus noted, they ate slowly for a few minutes. Albus left a glass of orange juice and wasted away from eating his own bread.', editor=laura,
        liked_by=[lindsay, laura, anna],
        rating=9)

    words_one = Writing(
    title='love and stuff verse',
    text='"I am jell the small parts of the rock that surronds you around you what do the flashes \n women  \n do without alot of lugage \n glue \n before they reprsent it. Gods fingers, tares and tares of small fury tings, wat today seems to be flowers are not to make pome by HIMSELF and have not lost it yet.',
    categories=[romance, personal],
    author=sheema
    )
    words_two = Writing(
    title='oh dear',
    text=' Then, after 1919, I was on a two-way trip from Cape Town to London. Enter 11 hours for entertainment online as you know. Our service was very difficult during the visit and it was very difficult to make it popular. The hotel is north of BA 20. After live activity, we found that education systems were not working. We started, but the police told us that they were working with this system after the Greg Underview system. After trying to spend from three minutes to 45 minutes, I heard many passengers know what to do in this way. Among them are vampires, grief and protection of our work, especially in Medelia and Phillip. I heard the passers-by saying that the situation was unfair and that they were undaunted. Each member has more accidents for two hours and has never been found. Eventually, Greg talked to any influential person and apologized for the matter. I told you that we understood that his staff were inaccurate, and we hoped them. We complained and told us to get the payment. I wish to talk about success, this was a stunning reaction to the BA 11, confirming that the plane was "very difficult" and "all", but when it was upset, British airlines reduced their scientific practices. Their rates are on the seats. We provide basic needs. In the 11th and 11th days, when the merchant returned to the boat, he was a seller who sought the passengers and knew basic needs, such as alcohol. At the end of the trip, Matilda\'s guests took a few steps. However, some of the features given to us were taken away and they were gone. Then, Filipp\'s tea. They were delighted, and Phillip responded, I did not find my suggestions on looking up or working.At the same time, during the sale, I heard something strangely unusual about other foods. It\'s a bad experience to start from the beginning to 20 years.',
    categories=[business, formal, complaint, feedback, suggestion],
    author=tom
    )
    words_three = Writing(
    title='Job ap!',
    text='Appleby: You can be able to read a new subscription. Apart from everyday business opportunities, good works of teamwork and guidance, I have been made good like from the MithIntyre Bar and Grill. The General Discussion n chit chat and that of your own experiences, gardens, wars and spirits, and for preparing some of the ready trades for this type of role. Competition management, administration and managmnt of peeple ho are able to do this. I can do educaton skills to protect a clean and secure environment, and have the right to communicate and talk and manage the time. Mines: Minor residents of mine acceptance and acceptance of food items, save food and drink, pay money and make money, protect and transfer money. It also has many rectangular functions. Help assist executive executives create whole-hearted business services and improve the health care needs. Building myself and planning, specialty management and specialty specialty specialties and tips for business staff and new consumer food. If I have a new experience of experience, my strength, New York\'s capabilities and discrimination, I would like to show my role in my role. I hope this ocupation is good!!!!!! cherrs, hamish Horesdale',
    categories=[work, cover_letter, CV, formal, application, business, request],
    author=mia
    )
    words_four = Writing(
    title='Letter of Gratitude',
    text='This letter describes the action taken regarding complaints of sexual harassment against John Doe. Mr. Doe was notified by letter of the complaints, and he met with me April 12 for further discussion of the matter. We reviewed the specific nature of each complaint originating in the accounting department and carefully examined company policy on each issue. Mr. Doe was informed that his employment with Doe Corporation would be terminated if more substantiated complaints of this nature were received. He has agreed to attend classes given by the human resources department to help him be more aware of the types of behaviors that may be offensive to others.',
    categories=[personal, family, thank_you],
    author=sim
    )
    words_five = Writing(
    title='Sonnet',
    text='If u wer crazy, I\'d go out in the sun. I run the tor late at nite so I can keep it in good lite. If u r in my world, I hav da lite of nite, the silent boundry, the dark of fortnite. Are 2 groups sumtimes turn are dances into dances. If you are on my island, I will be on my bitch and keep the see slow and tidy. This series contains sand dunes, but now with the storm I luv the soft vew. If u promiss 2 luv, I will be on time. But we are manz, but this is the luv of lurve, and this is my forever not to pie u Valentine.',
    categories=[romance, personal, family],
    author=talha
    )
    words_six = Writing(
    title='Application',
    text='Dear Felix, SUP DUDE? On behalf of my representative, I love you and everyting you do and I believe in myself. When a service is issues, the man says he needs a person to assist him in both aspects of the project. My current role as auxiliary support. I am a key player between my team and team so that I can focus on minimizing activities my chance to reduce self and reduce my choices. To continue this activity, you will learn to benefit others. Wechsler 7% class. It also uses direct connection with meetings, meetings, and preparation of the man. This file is recommended for advisory plans when discouraged. Thank you for reviewing your application. Lots of love, Elena Bizanthrope',
    categories=[work, business, CV, cover_letter, application],
    author=shane
    )
    words_seven = Writing(
    title='ME!',
    text='A money maker money making boss- THAT\'S WHAT I AM!, I offer flexibility and MONEY MAKING to make things go bOOM BOOM BOOM, enabling staff to make so much MONEY. Seriously, I AM SO GOOD.',
    categories=[business, formal, work, CV],
    author=kasia
    )
    words_eight = Writing(
    title='Complaint about burger',
    text='Oh come on this is ridic! I went to restaurant at 341 Hampton Rd. Friday, June 6. We arrived at 11.45. Ihave the invoice as proofo youeah??? so deon\t deny it!!! This is the nearest office. We met at least five times last year. Our Friday experience was a no brainer. We are not satisfied with chastity and curiosity. All the garbage tables are dirty and full of junk and junk. In addition, the house cleans the floor. The bathroom is not very clean. Previously, the restaurant was clean. We enjoyed Tacos joy. Mabes if you make things better. We usually visit at least once a month. Hide me. Thanks for the answer. Hi to you, William McPurry',
    categories=[complaint, formal, business, suggestion, criticism, feedback],
    author=ola
    )
    words_nine = Writing(
    title='Would like to be a teacher',
    text='My inspo for dance lessons came from the same affect that leaded me to my dance career nearly 13 years ago." Since the start place of my education in the artistic things, I have tried to use the language of the body to tell stories And feeling in the new language, and I became a strong supporter of teaching others. Throughout my career, I have seen dancing One to increase the life of dance and drama, and as my dad, I see students learn different kinds of dance and follow their creative expression, believe in fake compliments. Dancing is the first experience to develop the perspective of people who are interested in creating their own experience of creative, creative and creative. Believe me. Attempting my experience is related to ... A group of dancers ages 4 to 14 yrs old as a young dancer, Beck Cred studio studio. Dance and activities make the students happy!!!!! Introduce tips, music and music for students to experience.  In giving information about the dance style Adults with a fascinating story and discussion by using various teaching methods for each group. Manage different administrative tasks, including parental, scheduling, and payment communications. I got my MFA to dance at the MFA College and an introductory level in Natural Dance as a graduate assistant. San Francisco Spark Temp has been working for 13 years as a painter, artist, journalist and guest speaker (for a complete list of testimonials and art available upon request). My deep experience as a professional dancer and to inspire new and varied singers, I have successfully delivered Chrysalis Dance. I look forward to discussing my position and my advantages. Thanks for your attention. \n \n Lots of Love, Martha Greenpark',
    categories=[work, CV, application, business, formal_communications, formal, request],
    author=charlie
    )
    words_ten = Writing(
    title='don\'t like that choc',
    text='I do not want to beleeve that the last choclate bar has a different taste, so it\'s different, so I look online to see how other people have had a lot of negging after changing the same formula. iv eaten this choc long time, Im not interested now! I have a little pie for a cup ... I willn\'t buy another brand from now on to find D The correct formula is no different, and it does not break with the dark chocolate.',
    categories=[formal, feedback, complaint, business],
    author=daniela
    )
    words_eleven = Writing(
    title='bad experience in eatery',
    text='Dear Sir, I went to the restaurant on September 10, 2013 for dinner with my family. We ordered Chinese food and saved the waitress in early spring. If you wait a long time, your browser has expired. He reported this to his boss, but he was shocked when he refused to acknowledge and said he should find another restaurant. The children started to complain about the wrongs and we took them to the hospital. Your doctor has reported a food poisoning. Timely medical care. We encourage you to investigate your merits and cheats and take action on your service personnel. I will send you a copy of the invoice asking you to return the case. Thanks (or not!)',
    categories=[formal, feedback, complaint],
    author=jack
    )
    words_twelve = Writing(
    title='make me your coder',
    text='TLDR? HIRE ME, HERE IS WHY! I AM SO GOOD WITH COMPUTERS AND KNOW LOTS!!!!!!! \n \n \n Use the article for information about this article and the best information for your information. If you like checking / XML / PLSL, look for product support? Send cable that requires product support. You can get a lot of products in the best place for new service languages ​​and you can get a character for it. Click here to see this article in this article for more information about your name or name targeting visually. We can post this article for your article in protecting your website. We can post this article for more information on this article. Click here to see this article in Germany. In the past five years, an exclusive article in the best place has the best position in the Internet language. Log in to your Account Manager. You can log in to your Account Manager. We can get this article on the web. Bracken Mist Hadden ',
    categories=[work, application, business, CV],
    author=wes
    )
    words_thirteen = Writing(
    title='ad for me to do language speaking same with person',
    text='I want  meet someone who will do English, I do vietnamese and now do not have a great experience!',
    categories=[language, education],
    author=cliff
    )
    words_fourteen = Writing(
    title='busniness info ',
    text='Known and combined fruits with eleven new products from around the world, Delley Wesley Adapters, Walnut, Coconut Oil and Glasses are the 11 new ones to choose from. a wide range of branded products, launched exclusively in the Western markets of 2012, and will highlight new results in the coming months with almond oil cashew and cashew oils and extra 28 White oil. Walnuts Wesley Gold, co-founder of Wesley Gold, said: "I am very pleased to introduce Walnut Petroleum Products to a Southwest Company." "We gave 11 new products, not just one but two new nut fruits, fresh scents, and fresh ingredients that distinguish fruits and sugar. Wait until you get the Maphe Cashew taste." My bones are my new favorite creation!',
    categories=[business, formal, branding, press_release, journalism],
    author=gae
    )
    words_fifteen = Writing(
    title='Bit of writing about dead old person',
    text='Ms Margaret, who has lived in the Hull area for a long time, died Wednesday, May 18 at Sun Bridge Health Center. In 1928 Hull, SD, Margaret received her Bachelor of Science in Nursing from Hull University School of Medicine in 1991. She continued her education at Hull University, where she attended. Received his MD in Nursing in 1955. Margaret enrolled at Hull University in Amsterdam in the mid-1960s and worked in nursing homes in Massachusetts in 1970. She received a post as a librarian at Hull University of Technology. County, where he worked until his retirement. Margaret loves good food and flowers, enjoys movies and games with friends, and has a great smile that can shine in a room. Her grandmother, Tablia Winslow and many of her grandparents, all living in south Hull, have fun in the coming years. Memories can be a gift to human society in the Eternal Cave. Douglas work, stop slot.',
    categories=[personal, formal, obituary, journalism],
    author=kelsey
    )

    words_sixteen = Writing(
    title='Play thing',
    text='The Theater People are so happy to announce a version of  As You Like It Against the Background of New York City during the Great Depression. He held court-appointed discontent presentations for Hooverville from Arden, Rosalind, Orlando and their colleagues making love and talking about class conditions in a war place. Working words, music, and a pair of very very very very  comics make it one of Shakespeare\'s favorite hilarious plays',
    categories=[journalism, press_release, formal, branding ],
    author=brendan
    )

    words_seventeen = Writing(
    title='apologies',
    text='I feel that you really deserve massive sorry! Personal apologies for the meeting yesterday. I know these days because I\'m sorry. I hope you can forgive me. I have a great honor to work with you. Sorry. Sorry Please ...',
    categories=[formal, apology, personal, work, business],
    author=amy
    )
    words_eighteen = Writing(
    title='Short Story',
    text='On the morning of June 27, the heat was clear all summer. Too much peace and green grass. The man stopped for ten minutes at the post office and the bank. Many people started working in the city on June 2 for two days. There were only three hundred people living in rural areas and the crisis went down for two hours, so that the morning started at ten and the villagers needed food. After the chat boy. It was a summer school and often surrounded his independence and quickly started working. And teachings on class and teacher, books and titles. Bobby Martin picked up his stones and quickly and easily received other children to get the most beautiful and bright stones. Bobby and Harry Jones and Dickie Dellcrovey - people in the village say - have finally been built in forest areas and other children protected by the ceasefire. Boys are different, talking, looking at their stones, robbing or becoming strangers to their ancestors. Talk about kids, forests and mountains, tractors and tax collection early. They stood around the rock, gathered around the boat, replaced instead, were quiet and quiet. Womens clothing and bedding are near their time.',
    categories=[business, formal],
    author=sheema
    )
    words_nineteen = Writing(
    title='Letter on front of job app',
    text='I noticed that my inbox (embarrassing!!!!!) holds 150000000 unread messages, including at least 5000 different type newsletters. But this only creates an email that is worth the opening. In my opinion, the use of your job is a real advantage. I\'ve been following Vitabe for a number of years, and I can say that I\'ll return any email you send me. I have a good cube for a good subject line - "Vitamin A is over - our favorite thing with ABC with my" favorite "- and how your email content feels fun and expert help, talking for the reason I I am glad to present your request to the email marketing email address of your company, I have four years of marketing experience, my current role at West Side Bank is to provide email designs. New data for new customers is analyzed and Analyze data on different types of customers that change with people who have already received money, as well as the results of the A / B survey and tourism maps. We interacted, we were able to pay. And 30% of these subscribers, as our result would be significantly higher than last year, I also focused on credit reports to educate my clients about How they manage and manage their records that have the highest record',
    categories=[work, business, application, formal, CV, cover_letter],
    author=gae
    )

    words_twenty = Writing(
    title='Fan Fiction',
    text='Albus moved under his blankets. His leg was torn off his plate (how did this happen?), And he sat in his bed, so that sunlight flowed through his window. She looked at art, who slept slowly in a sleeping bag on the floor. How did the person get the best sleep on earth? Albus felt sweaty and sad. His neck bent slightly. He must have laughed at her. Al up and down stairs, where mom and James ate breakfast. Her usual home is boring - she left yesterday Atlantis, after a day trip around the city. "I think Father and Lily are still sleeping?" Albus asked: He is tied up in the chair.  "Indeed, neither is Lily still asleep, but your father at work, the mother answered." But I thought Dad with us came to Diagon\'s Alley today! "It\'s their program they have two days in the World Cup, the next day It started on Diagon alley, and then art to school, but your Dad wanted to go with them on the Diagon , which was supposed to fall with us, but at an hour after this second morning, your father "What happened to you?" "What did he say to you?" James asked enthusiastically: "We do not say that they still do not know much. There was no strong evidence from this morning.""A strong certificate From what? " James asked, "Come on, mother, please?" Albus asked what was exciting to drag her father in the morning of her Diagon alley trip. Probably you will see the evening prophet tonight tonight. Oh, so, enough for the Prophet\'s version of the important era? "It\'s possible that the exciting news that was published during the day that the Prophet Muhammad was published the next morning," James excited. Otherwise, surely it will be on the morning of the day. So you have to fill your breakfast today. Aunt Hermione, Rose, and Hugo in the liquid kettle this morning, right? about two hours, I think." Albus noted, they ate slowly for a few minutes. Albus left a glass of orange juice and wasted away from eating his own bread.',
    categories=[fan_fiction, prose, short_story ],
    author=cliff
    )
    redone_one = Edit(title='For You', original=words_one,
    text='I am jealous of the sand\n beneath you \n around you \n what you see \n bright things \n  erased lady \n sparkling and traveling without luggage \n liquidity \n before X \n you are tattooed on my back \n music \n dies down \n I too grew up in \n the soft hands \n of the gods \n and a little donkey will lead them \n Tears, tears, and I know \n just what they mean \n honeysuckles at night \n  I wrote this poem for you and haven\'t lost it',
    editor=lindsay,
        liked_by=[anna, laura],
        rating=2)

    redone_two = Edit(title='Letter of Complaint to British Airways', original=words_two,
    text='To whom it may concern, \n \n I am writing to complain about our flight from Cape Town to London Heathrow on 19/04/19.  As you will be aware, our in-flight entertainment did not work for the entirety of the 11-hour flight. Our cabin crew were rude and unhelpful throughout the flight, making it a hugely unpleasant experience. I am extremely disappointed with the £20 voucher response and do not think this is sufficient compensation for the errors made by BA. \n \n After immediately boarding the place, we noticed that the in-flight entertainment system was not working. We had not yet taken off, but the cabin crew informed us that it was only possible to do a system reset after take-off. We were told that this would resolve the issue.  Greg Underwood, the Customer Relations Manager, asked that we let her know if the system reboot had not worked. After three attempts, and nearly 45 minutes without being updated, I heard several other passengers asking the cabin crew if the issue would be resolved. They were met with annoyance, frustration and a defensive attitude from our cabin crew - namely, Matilda and Phillip. I heard Matilda say to the inquiring passenger that the situation was “unfair” on staff and she walked away without apologising.  Both members of the cabin crew ignored the issue for over two hours and we had still not received an apology. \n \n Eventually, Greg spoke with each row of affected passengers and apologised for the issue. I informed her that we felt as if cabin crew had ignored the situation and that more could have been done to apologise.  We received the complaints leaflet and were informed we would receive compensation. \n \n I would like to take the opportunity here to add that while she was speaking to a passenger behind me, who had spent the previous 11-hour BA flight with broken screens, Greg admitted that the plane was “very old” and that the screens “break all the time”. In an era where low-cost flights are readily available, passengers choose to pay extra for the reputation and comfort of British Airways. I am shocked and appalled that a company with the reputation of British Airways would knowingly allow for passengers to spend their money on seats that do not have the basic amenities that we pay for. \n \n In addition to the broken screens during the entirety of our 11-hour flight, the cabin crew were rude and unpleasant to my family and to other passengers around her. Phillip in particular was evidently very unhappy. Throughout the flight, she snapped at passengers and did not offer to help with our basic requests, such as drinks.  At the end of the flight, Matilda was pouring coffee for passengers. However, she stopped a few rows ahead of ours and did not return. A while later, Phillip returned with tea. The passengers in the row behind asked politely for coffee, to which Phillip replied, “Coffee has already been down here”. She did not offer to get more or apologise for the fault of the cabin crew.  As well as this, during the flight, I heard another passenger become very upset because her meal had not been put on to the plane. \n \n It is clear that both the cabin crew and the plane were not prepared for the flight. It was horrible experience from start to finish and one that absolutely requires more than a £20 voucher to compensate. \n \n I look forward to hearing your response and your suggestion for a more suitable compensation for all four members of my party.',
    editor=alex,
        liked_by=[lindsay, laura, anna],
        rating=8)

    redone_three = Edit(title='Bar Job Application', original=words_three,
    text='Miss Appleby: After reading about your need to be a new member, you can join me. In addition to providing excellent clients with casual and classy dining experiences, having a good knowledge of team collaboration and leadership, I greatly benefit from this role at McIntyre Bar and Grill. General Discussion \n My experience in preparing and transporting cocktails, beer, wine and spirits to different clients has prepared for this role. My ability to achieve this capability is government preparation, inventory management, and managing people. I can produce faulty alcohol while maintaining a clean and safe environment, and have the ability to interact and communicate and manage time. Examples of my background are: The Hygiene Line takes customers and orders, delivers the right food and drink, collects and makes money, maintains excellent inventory levels, and quickly. It also balances several restaurant functions. enables managers to create a full range of operational tasks and provide better customer satisfaction support. \n Demonstrate team building and planning skills, strong leadership skills and unique interpersonal skills, tips for new employees in regular bar and restaurant operations. If my past experience and enthusiasm and ability, and the neutrality of New York, I would like to highlight my expectations for this role. I look forward to discussing this post in more detail. Thanks for looking. \n Unfortunately, Horsehead',
    editor=lindsay,
        liked_by=[lindsay, laura, anna],
        rating=10)

    redone_four = Edit(title='A Wedding Thank You', original=words_fourteen,
    text='“From the bottom of our hearts we would like to thank you for celebrating our special day with us and making it the most memorable day of our lives. From sweating it out together during the ceremony, to dancing the night away in the rain, we definitely felt the love from you all on the day. \n \n We can’t wait for our trip to Europe at the end of July, which wouldn’t be possible without all of your generous gifts.\n \n We look forward to starting the next chapter of our lives together and sharing many more memories with you all!”',
    editor=lindsay,
        liked_by=[anna, lindsay, ollie, alex, harry, laura],
        rating=18)

    redone_five = Edit(title='Valentine', original=words_five,
    text='If you were crazy, I\'d go out in the sun. I run the tour late at night so I can keep it in good light. If you are in my world, I have the light of night, the silent boundary, the dark of night. Our two groups sometimes turn our dances into dances. If you are on my island, I will be on my beach and keep the sea slow and tidy. This series contains sand dunes, but now with the storm I love the soft view. If you promise to love, I will be on time. But we are human, but this is the love of love, and this is my forever faithful Valentine.',
    editor=anna,
        liked_by=[anna, lindsay, ollie, alex, harry, laura],
        rating=18)

    redone_six = Edit(title='Application For Position of Personal Assistant', original=words_six,
    text='Dear Mr Darling, \n \n Please find enclosed my application for the role of personal assistant. I found your job posting on indeed.com , and I believe that my experience and skills make me the perfect candidate for this position. \n \n Your job posting states that your company’s CEO requires an experienced personal assistant to support her in all aspects of her work. \n \n In my current role as personal assistant to Ms. Miseldoon, CEO of Blue & White, I act as the primary gateway between her and her team, ensuring that she can focus on the tasks that require her personal attention while minimizing the scope for distractions. In this way, I have successfully increased Ms. Wexler’s productive time by 7%. \n \n Additionally, I harness my communication and interpersonal skills to liaise between departments, scheduling team meetings and conference calls for Ms. Romper. Because of my ability to multitask, Ms. Hale has entrusted me with keeping minutes for such meetings. \n \n I also spearheaded Blue & White’s 10-minute stand-up meeting initiate that has boosted workplace efficiency by reducing wasted time. \n I am looking forward to hearing back from you. Thank you for considering my application. \n \n Sincerely, \n \n Felina Bysanthrope',
    editor=anna,
        liked_by=[anna, laura],
        rating=7)

    redone_seven = Edit(title='PBS', original=words_seven,
    text='An entrepreneurial and entrepreneurial leader, I offer flexibility and entrepreneurship to foster good growth and good entrepreneurship, enabling staff to achieve high production. And increase a business, trustworthy and trustworthy. My plan for managing calm is to make people better understand, proud, and motivated to become the best in the industry.',
    editor=anna,
        liked_by=[anna, lindsay, ollie, alex, harry, laura],
        rating=19)
    redone_eight = Edit(title='Letter of Complaint to Fast Food Establishment', original=words_fourteen,
    text=' Dear Mrs. Artengrowth, \n \n My coworkers and I recently visited the Mysterious Meat restaurant at 341 Hampton Rd. on Friday, June 6th. We arrived at about 11:45. I have enclosed a copy of my receipt for your convenience. \n \n This location is close to our office. We have met there at least five times within the past year. However, our experience on Friday was not a positive one. We were unhappy with the cleanliness and felt you needed to be made aware of the situation. All of the unoccupied tables were dirty and littered with crumbs and trash. In addition, the floor appeared to need mopping. The bathrooms were not very clean as well. \n \n In the past, the restaurant has been clean. We really do enjoy the food at the Happy Taco. If improvements are made, we would be more likely to meet there again in the future. We typically visit at least once a month. \n \n Please feel free to contact me. Thank you for your response. Have a good day. \n \n Sincerely, \n \n Willam Makepeace',
    editor=anna,
        liked_by=[anna, lindsay, ollie, alex, harry, laura],
        rating=21)
    redone_nine = Edit(title='Dance Teacher Cover Letter', original=words_nine,
    text='My motivation to teach dance derives from the same impulse that led me into my fulfilling dance career nearly 13 years ago. Since the beginning of my studies in the performing arts, I have sought to use physical movement to express stories and emotions in innovative ways, and I am a strong proponent of teaching others how to do the same. Throughout my career, I have consistently viewed dance as a way to enrich both performers’ and viewers’ lives, and I believe my obligation as a dance teacher is to encourage students to learn a variety of dance styles and pursue their own creative expression. Having experienced first-hand the power of dance to shape people’s perspectives, I am enthusiastic about using my professional experiences, skills, and beliefs to educate new young dancers in the techniques and movements of creative dance. \n \n Highlights of my experience include… \n \n Leading groups of young dancers ranging in age from 4 to 14 for the past six years as an instructor with the Berkeley Dance Studio; demonstrating dances and movements, making suggestions to students, monitoring performance, and introducing new artistic and musical elements to keep students engaged and excited. \n \n Applying different and appropriate teaching techniques for each age group while also providing information about the origins of particular styles of dancing to older students through interesting stories and discussion. \n \n Handling various administrative tasks, including parent communication, schedules, and billing. \n Achieving my MFA in Dance from Mills College and teaching an entry-level course titled “Introduction to Creative Dance” as a graduate assistant. \n Performing with the San Francisco Spark troupe for the past 13 years as a dancer, choreographer, producer, and media spokesperson (a full list of articles, references, and quotes available upon request). \n With my keen ability to develop and evolve new dancers, combined with my in-depth experience as a professional dancer, I am prepared to excel in providing excellent instruction at Chrysalis Dance Studio. I look forward to discussing the position, and my qualifications, in further detail. Thank you for your consideration. \n \n Sincerely, \n \n Martha Greenpots',
    editor=anna,
        liked_by=[anna, lindsay, ollie, alex, harry, laura],
        rating=21)
    redone_ten = Edit(title='Cadburys New Recipe Feedback', original=words_ten,
    text='I cant believe why my last few bars of chocolate tasted so different (threw some out). So, I looked online to see if others had experienced the same to find many negative reviews after a change in recipe. I\'m in my 60\'s and have used Cadbury\'s for most of this time. I\'m NOT impressed! I only have a few pieces with a cuppa for dessert... no more as will be buying another brand from now on after finding out that the actual recipe is different- not old nor spoilt chocolate',
    editor=anna,
        liked_by=[lindsay, laura, anna],
        rating=9)
    redone_eleven = Edit(title='Letter Concerning poor Service at Restaurant', original=words_eleven,
    text='Dear Sir,\n visited your restaurant on 10 September 2013 for dinner with my family. We ordered Chinese food and requested the waiter for spring-rolls first. \n The starter came in after a long wait and turned out to be stale. Despite reporting the same to your supervisor, he denied our claim and was rude when he asked us to look for another restaurant instead. \n \nThe children started complaining of discomfort and we rushed them to a hospital wherein doctors declared food-poisoning. We could avert serious damages due to timely medical attention. \n \n I request you to kindly investigate and take action against the staff on duty for their negligence and rude behavior. I am sending a copy of hospital bills for reimbursement failing which I will take up the case to the Customers Forum for stringent action against your restaurant. \n \n Thanking You, \n \n Graham Short',
    editor=anna,
        liked_by=[anna, laura],
        rating=9)
    redone_twelve = Edit(title='Letter providing coverage about web dev', original=words_twelve,
    text='Use the article for information about this article and the best information for your information. If you like checking / XML / PLSL, look for product support? Send cable that requires product support. You can get a lot of products in the best place for new service languages ​​and you can get a character for it. Click here to see this article in this article for more information about your name or name targeting visually. We can post this article for your article in protecting your website. We can post this article for more information on this article. Click here to see this article in Germany. In the past five years, an exclusive article in the best place has the best position in the Internet language. Log in to your Account Manager. You can log in to your Account Manager. We can get this article on the web. Bracken Mist Hadden ',
    editor=laura,
        liked_by=[lindsay, laura, anna],
        rating=9)

    redone_thirteen = Edit(title='Vietnames/English Language Exchange', original=words_fourteen,
    text='I want to meet someone to practice English with me, right now I only have a very basic level (I have had help to write this!) I can teach you Vietnamese in exchange! ',
    editor=laura,
        liked_by=[anna, lindsay, ollie, alex, harry, laura],
        rating=8)

    redone_fourteen = Edit(title='Nut Butter Start-Up Press Release', original=words_fourteen,
    text='Leading Nut Butter and Confections Brand Launches Eleven Out-of-this-World New Products \n Wesley’s, maker of naturally delicious, high-quality nut butters, nut butter snacks and organic peanut butter cups, today announces 11 new SKUs of great tasting products to the brand’s extensive and admired nutty family. Officially being unveiled at this year’s Natural Products Expo West and rolling out on shelves over the course of the next few months, Wesley’s welcomes new firsts for the brand including a line of Cashew Butter and Dark Chocolate Almond and Cashew Butter Cups along with tasty line extensions in White Chocolate Mini’s, 28 oz. Peanut Butter and Cinnamon Almond Butter. \n \n “Calling all astro-nuts! I couldn’t be more excited to share my new nut butter-fueled products all blasting off at Expo West,” said Wesley Gold, founder of Wesley’s. “We’ve landed on not one, not two, but 11 fantastic new products that round out our nut butter and confections lines with new nut types, new flavors and new forms. The nut butter snacking possibilities are endless, and deliver the damn good taste and high-quality ingredients that consumers have come to love and expect from the brand. Wait until you taste our Maple Cashew—it’s giving Maple Almond Butter a run as my new personal favorite!”',
    editor=laura,
        liked_by=[anna, lindsay, ollie, alex, harry, laura],
        rating=20)

    redone_fifteen = Edit(title='Margaret Deedward\'s Obituary', original=words_fifteen,
    text='Margaret, a long-time resident of the Hull area, died Wednesday the 18th of June at Sun Bridge Healthcare Center. \n \n Born in 1928 in Hull, S.D., Margaret received a Bachelor of Science in Nursing Education from South Hull State College in 1951. She continued her education at the University of Hull, from which she received her M.Ed. in Nursing in 1955. \n \n Margaret taught Nursing at the University of Hull at Amherst in the mid-1960s and worked at various psychiatric nursing facilities throughout western Massachusetts in the 1970s. In a career shift, she took a position as a librarian assistant at Hull County Technical School, where she worked until her retirement. \n \n Margaret loved good food and socializing, enjoyed going to movies and plays with friends, and had a wonderful smile that could light up a room. \n \n She is survived by her niece, Tabitha Winslow and several grandnieces, all of whom live in southern Hull, and brought great joy to her later years. \n \n Memorial gifts may be made to the Hull Valley Humane Society. \n The Douglass Funeral Service, Hull, has been entrusted with arrangements.', editor=laura)

    redone_sixteen = Edit(title='Press Release for Production of As You Like It', original=words_sixteen, text='The Theatre People is pleased to present As You Like It against the backdrop of New York City during the Great Depression.  Shedding the opulence of the court for the Hooverville of Arden, Rosalind, Orlando and their co-mates explore the nuances of passion and classism in a pre-war setting.   Word play, music, and a couple of classic clowns make this one of Shakespeare’s best-loved comedies.', editor=laura,
        liked_by=[anna, lindsay, ollie, alex, harry, laura],
        rating=20)


    redone_seventeen = Edit(title='Letter of Apology', original=words_seventeen,
    text='I feel I owe you a personal apology for my insensitive comment at the meeting yesterday. I know these days since John\'s funeral have been very difficult for you, and I was clearly out of order in making reference to "merry widows." I\'m sorry you had to suffer from my foolishness. \n \n I hope you will be able to forgive me. I have tremendous respect for you and your abilities, and I hope we can continue to work well together. I\'m terribly sorry.',
    editor=laura,
        liked_by=[anna, lindsay, ollie, alex, harry, laura],
        rating=20)

    redone_eighteen = Edit(title='The Game', original=words_eighteen,
    text='The morning of June 27th was clear and sunny, with the fresh warmth of a full-summer day; the flowers were blossoming profusely and the grass was richly green. The people of the village began to gather in the square, between the post office and the bank, around ten o\'clock; in some towns there were so many people that the lottery took two days and had to be started on June 2th. but in this village, where there were only about three hundred people, the whole lottery took less than two hours, so it could begin at ten o\'clock in the morning and still be through in time to allow the villagers to get home for noon dinner. \n The children assembled first, of course. School was recently over for the summer, and the feeling of liberty sat uneasily on most of them; they tended to gather together quietly for a while before they broke into boisterous play. and their talk was still of the classroom and the teacher, of books and reprimands. Bobby Martin had already stuffed his pockets full of stones, and the other boys soon followed his example, selecting the smoothest and roundest stones; Bobby and Harry Jones and Dickie Delacroix-- the villagers pronounced this name "Dellacroy"--eventually made a great pile of stones in one corner of the square and guarded it against the raids of the other boys. The girls stood aside, talking among themselves, looking over their shoulders at rolled in the dust or clung to the hands of their older brothers sisters. Soon the men began to gather. surveying their own children, speaking of planting and rain, tractors and taxes. They stood together, away from the pile of stones in the corner, and their jokes were quiet and they smiled rather than laughed. The women, wearing faded house dresses and sweaters, came shortly after their menfolk.', editor=laura,
        liked_by=[anna, lindsay, ollie, alex, harry, laura],
        rating=11)

    redone_nineteen = Edit(title='Job Application Cover Leter', original=words_sixteen, text='I noticed that my inbox (and embarrassing) holds 1500 unread messages, including at least 50 different type newsletters. But this only creates an email that is worth the opening. In my opinion, the use of your job is a real advantage. I\'ve been following Vitabe for a number of years, and I can say that I\'ll return any email you send me. I have a good cube for a good subject line - "Vitamin A is over - our favorite thing with ABC with my" favorite "- and how your email content feels fun and expert help, talking for the reason I I am glad to present your request to the email marketing email address of your company, I have four years of marketing experience, my current role at West Side Bank is to provide email designs. New data for new customers is analyzed and Analyze data on different types of customers that change with people who have already received money, as well as the results of the survey and tourism maps. We interacted, we were able to pay.% And 30% of these subscribers, as our result would be significantly higher than last year, I also focused on credit reports to educate my clients about How they manage and manage their records that have the highest record', editor=laura,
        liked_by=[anna, laura],
        rating=8)

    redone_twenty = Edit(title='Harry Potter Fan Fiction', original=words_twenty, text='Albus shifted under his blankets. He untangled his leg from his sheet (how did that happen?), and sat up in his bed as sunlight streamed through his window. He glanced down at Art, who was sleeping soundly in a sleeping bag on the floor. How was it that the person on the ground had the best sleep? Albus felt sweaty and uncomfortable. His neck ached slightly. He must have slept on it funny. Al got up and crept downstairs, to where Mum and James were eating breakfast. It was his ordinary, boring house- they had left Atlantis yesterday, after spending a day touring the city. \n \n “I presume Dad and Lily are still sleeping?” Albus asked, as he plopped down on a chair. \n \n “Actually, no. Lily’s still sleeping, but your father’s at work,” Al’s mum replied. \n \n “But I thought dad was coming with us to Diagon Alley today!” Albus said. That was the plan. They were going to spend two days at the World Cup, the day after that at Diagon Alley, and then Art was going back until school started. But dad was planning to be with them at Diagon Alley.\n \n “He was supposed to come with us, but at an unearthly hour this morning, your father was called into work. A few minutes later, I got a ten-second brief of what was going on.” \n \n “What did he tell you?” James asked eagerly. \n \n “Not telling. They don’t know much yet. As of this morning there was no hardcore evidence.” \n \n “Hardcore evidence of what?” James asked. \n \n “Come on mum, please?” Albus begged. Something that dragged his dad out on the morning of their Diagon Alley trip had to be exciting. \n \n “Sorry. You’ll probably see it in The Evening Prophet tonight anyway.” \n \n “Oooh, so it’s important enough for an edition The Evening Prophet?” James said excitedly. The Evening Prophet was only issued if there was exciting news that happened over the course of the day. \n \n “Possibly. If not, it will definitely be in the news tomorrow morning. Anyway, enough about that, you need to fill up on breakfast for our trip today.” \n \n Knowing that he would not be able to get anything else out of his mum, Albus asked, “We’re meeting Uncle Ron, Aunt Hermione, Rose, and Hugo at the Leaky Cauldron this morning, right?” \n \n “In about two hours, I believe.” Albus nodded. \n \n They ate in silence for the next few minutes. Albus gulped down a large glass of orange juice, and resumed eating his toast.', editor=laura,
        liked_by=[anna, lindsay, ollie, alex, harry, laura],
        rating=8)

    redone_one_two = Edit(title='This Poem Is Intended For Yourself', original=words_one,
    text='I am envious of the small pieces of rock\n under yourself \n surrounding yourself \n what you purvey \n sparkling elements \n  rubbed out woman \n shining and going without copious quanitites of baggage \n viscous material \n before the thing that marks the spot \n your name is written in biro upon my shoulder blade \n musicality \n perishes downwards \n I too grew up in \n the soft finger plates \n of the deities \n and small equine mammal \n Tears, tears, and I am aware \n just what they seem to signify \n flowers not in the day \n  I have done this poem FOR YOURSELF and haven\'t mislaid it (yet)',
    editor=laura,
        liked_by=[anna, lindsay, ollie, alex, harry, laura],
        rating=8)
    redone_two_two = Edit(title='Complaining To British Airways', original=words_two,
    text='To whom it may concern, I write to say bad things from two trips from Cape Town to London Heathrow on 19/04/19. As you know, the entertainment did not succeed on board the entire flight for 11 hours. Our crew was rude and unhelpful throughout the trip, making it a very unpleasant experience. The hotel is located in the north section of BA 20 LE per coupon. \n \n After riding the place directly, we noticed that the onboard entertainment system was not working. We did not take off yet, but the cabin crew told us that it was possible to reset the system after Greg Underwood, the customer relations manager, told her that the system was not working. After three 45 attempts and about 45 minutes without updating, I heard many other passengers asking the cabin crew what to do. They were met with the frustration, frustration and defensive attitude of our cabin vampires - specifically Matilda and Philip. I heard Matilda telling the inquiring passenger that the situation was "unfair" to the staff and she moved away without apologizing. Each of the crew members ignored the case for more than two hours and we have not received any apology yet. At the end, Greg spoke to each of the affected passengers and apologized for the problem. I told her that we felt as if the cabin crew had ignored the situation and that much could have been done to apologize. We received a complaints bulletin and informed us that we would receive compensation. \n \n nI would like to take this opportunity here to add that while she was talking to a rear passenger, who spent the previous 11 BA flight with broken screens, Greg admitted that the plane was "very old" and that the screens were "broken all the time". I am shocked and shocked that a company with a reputation for British Airways will deliberately allow passengers to spend their money on seats that do not have the basic amenities we pay for. In addition to the broken screens during the 11-hour journey, the cabin crew was rude and unhappy to return to the flight, picked up passengers and did not help meet our basic requests, such as drinks. At the end of the trip, Matilda was pouring coffee for travelers. However, a few rows were stopped in front of us and no Deedwarder. Later, Philip returned with tea. The passengers behind the coffee asked politely, and Phillip replied, "I did not make an offer to get more or apologize for the crew\'s mistake." In addition, during the flight, I heard another passenger very upset about not eating It was a terrible experience from start to finish and definitely required a large amount of £ 20 for compensation. My Yoni Yoni Ya Yoni Ya Yoni Ya Yoni Y Me',
    editor=harry,
        liked_by=[anna, laura],
        rating=8)
    redone_three_two = Edit(title='Applying to Become A Master of Alcolic Beverages, sutuated behind a Bar', original=words_three,
    text='Miss Appleby: After reading about your need to be a new member, you can join me. In addition to providing excellent clients with casual and classy dining experiences, having a good knowledge of team collaboration and leadership, I greatly benefit from this role at McIntyre Bar and Grill. General Discussion \n My experience in preparing and transporting cocktails, beer, wine and spirits to different clients has prepared for this role. My ability to achieve this capability is government preparation, inventory management, and managing people. I can produce faulty alcohol while maintaining a clean and safe environment, and have the ability to interact and communicate and manage time. Examples of my background are: The Hygiene Line takes customers and orders, delivers the right food and drink, collects and makes money, maintains excellent inventory levels, and quickly. It also balances several restaurant functions. enables managers to create a full range of operational tasks and provide better customer satisfaction support. \n Demonstrate team building and planning skills, strong leadership skills and unique interpersonal skills, tips for new employees in regular bar and restaurant operations. If my past experience and enthusiasm and ability, and the neutrality of New York, I would like to highlight my expectations for this role. I look forward to discussing this post in more detail. Thanks for looking. \n Unfortunately, Horsehead',
    editor=harry,
        liked_by=[anna, lindsay, ollie, alex, harry, laura],
        rating=8)
    redone_four_two = Edit(title='Gratitude is the apt response in this circumstance (wedding attendance)', original=words_four,
    text='We thank you sincerely for celebrating your day with you and making it the most memorable day of your life. During the ceremony, I danced all day in the rain, sliding together, you felt the day of love. We can\'t wait to travel to Europe at the end of July, this can\'t happen without all your good gifts. \n We look forward to starting the next chapter of our lives and sharing more memories with you! "',
    editor=harry,
        liked_by=[anna, lindsay, ollie, alex, harry, laura],
        rating=15)
    redone_five_two = Edit(title='Be My Valentine', original=words_fourteen,
    text='If you were a fool, I was in the sun and when it rained I fell on the ground. I will change the tour late at night so that I can keep it in good light. If you are in my world I will be the light of the night in your moon, quiet boundary, darkness. Together, our two groups sometimes move our dance to dance. If you are on my island, I will be on your shore and clean the ocean softly and gently. This series assumes sandy beaches, but now with thunderstorms, I like soft scenery. If you promised to love, if the stars are not right I\'ll be in time. And we are people, but absolutely love is in love, and it will be my eternal loyalty to Valentine.',
    editor=harry,
        liked_by=[anna, lindsay, ollie, alex, harry, laura],
        rating=15)
    redone_six_two = Edit(title='Letter to Become PA', original=words_six,
    text='Dear Felix, I represent my agent, I am happy with your work and I believe in your experience and skills so that I can fill you as a candidate. When you advertise your service, it shows that the company\'s CEO needs his own experience to support all aspects of the project. My current role as a direct assistant. I act as a key gateway between him and his team to ensure that he can focus on actions that reduce his chances of personal attention and reduce his decision. To continue here, I see how to be successful with others. Wechsler courses are 7%. In addition, I use my communication and communication skills to edit meetings, meetings, and rockets. This belt gave me the protocol for such meetings because of my ability to intrude on swallowing. Listen, thanks for reviewing your request, so Elena Biszorp',
    editor=harry,
        liked_by=[anna, lindsay, ollie, alex, harry, laura],
        rating=13)
    redone_seven_two = Edit(title='My Brand', original=words_fourteen,
    text='A focused and purposeful business leader, I propose entrepreneurial persistence and wisdom to stimulate profit growth and profitable business, inspire employees to achieve maximum productivity and develop profitable business relationships based on respect, loyalty and trust. My calm sense of humor was the defining management strategy to bring out the best in everyone, instill pride and mobilize them to make their company the best in the industry.',
    editor=harry,
        liked_by=[anna, lindsay, ollie, alex, harry, laura],
        rating=6)
    redone_eight_two = Edit(title='Restaurant Complaint', original=words_eight,
    text='My wife and her wife, I recently visited a mysterious meat restaurant at 341 Hampton Rd. Friday, June 6. We arrived around 11:45. I\'ve added a copy of my invoice for your convenience. This is a place close to our office. We met there at least five times last year. Our experience on Friday is not positive. We are not happy with the purity and the sense of what you need to know. All deserted tables are dirty and full of rubbish and rubbish. In addition, the floor clean the house. The bathroom is not very clean. In the past, the restaurant was clean. We really enjoy having Happy Taco. If improvements are made, we are more likely to meet in the future. Usually we visit at least once a month. Contact me. Thank you for your feedback. Good day to you And frankly, William McPurry',
    editor=harry,
        liked_by=[anna, lindsay, ollie, alex, harry, laura],
        rating=13)
    redone_nine_two = Edit(title='I will be an excellent instructor of dance!', original=words_nine,
    text='My inspiration for teaching dance comes from the same influence that led me to my dance career nearly 13 years ago. Since the beginning of my education in the art of play, I have been trying to use body language to tell stories and emotions in new languages, and I have been a strong supporter of teaching others. Throughout my career, I have seen dance as a way to enrich the life of dance and theater, and as my dance teacher, I see students learning different types of dance and following their creative expression. Believe in motivation. I think dance is an early experience in shaping the perspectives of people, interested in developing their own experiences of creativity, creativity, and beliefs. \n \n Reviews of my experience include ... \n \n A group group 4 to 14 years ago as a young dancer as Berkeley Dance Studio coach; performs dances and activities, keeping students busy and happy. Introduce tips, observations, and art and music for students to observe. \n \n While providing information on adult dance style through interesting stories and discussions using a variety of teaching techniques for each group. \n \n Manage various administrative tasks, including parent communication, schedules and payments.  I am getting my MFA in Dance at MFA College and an introductory level course in natural dance as a graduate assistant. San Francisco Spark Temp has worked for the past 13 years as an illustrator, artist, journalist, and speaker (a full list of articles, testimonials, and art available on request). \n With my deep experience as a professional dancer and inspiring a new dancer and changing my skills, I have succeeded in providing Chrysalis Dance Studio. I look forward to discussing my position, and my qualifications further. Thanks for your attention. \n \n Sincerely, \n \n Martha Green Potts',
    editor=harry,
        liked_by=[anna, lindsay, ollie, alex, harry, laura],
        rating=13)
    redone_ten_two = Edit(title='Cadbury\'s Complaint', original=words_ten,
    text='I do not want to believe that the last chocolate bar has a different taste, so it\'s different. So I look at the web to see that others experience the same as getting many negative reviews after changing the formula. I\'m 60 years old and have used most Cadbury. I\'m not interested! I just have a couple of pieces for a cup of tea ... I will not buy another brand from now on finding the exact formula does not differ from the other and does not break with the chocolate ',
    editor=harry,
        liked_by=[anna, lindsay, ollie, alex, harry, laura],
        rating=13)
    redone_eleven_two = Edit(title='Restaurant Complaint', original=words_eleven,
    text='Dear Sir, I went to your restaurant on September 10, 2013 for dinner with your family. We ordered the Chinese food and asked the waiter for the spring rolls first. wait n The opener became obsolete after a long wait. He reported it to his supervisor, but he declined our comment and was horrified when he asked us to find another restaurant. \n \n The children started complaining about the discomfort and we took them to a hospital. Doctors declared food poisoning. Timely medical care can prevent serious harm. \n \n I urge you to kindly investigate your negligence and indecent behavior and take action against the service officers. I will send a copy of the hospital bill for a refund to take the case to the Consumer Forum to take strict action against your restaurant. \n \n Thanks, \n \n Graham Short',
    editor=alex,
        liked_by=[anna, laura],
        rating=13)
    redone_twelve_two = Edit(title='Web Dev Cover Letter', original=words_twelve,
    text=' Mr. Martina, N I recently read my latest release on Junior Web Developer. Focusing and focusing on detailed information and common understanding of HTML and Java / XML / PLSL is a special option. As a current entrepreneurship, I am certified and fully distributed according to the applications, fully design. Depending on the wording and the effectiveness of the advertising programs, we still add great code to the broadcaster\'s form. With all my caution and hard work, I have received general promotions and bonuses. I hold a Bachelor\'s degree in Information Technology and General Information and Certification. Can write great laws, speak clearly and work with partners. I\'m a 5 year old company specializing in business and I want to provide information about specialized companies. In all competencies, she is the exclusive representative of the Junior Web Developer position. Call to arrange an interview. I follow my body and look forward to the meeting. Against Brackensmist Hadden',
    editor=alex,
        liked_by=[anna, laura],
        rating=13)


    redone_thirteen_two = Edit(title='Start-Up Press Release', original=words_thirteen,
    text='I want to meet someone to practice English with me, right now I have only a very basic level (I have help to write this article!) I can teach you Vietnamese to exchange!',
    editor=alex,
        liked_by=[anna, laura],
        rating=15)
    redone_fourteen_two = Edit(title='New Nut Butter Brand Is Answer To Your Nutty Prayers!', original=words_fourteen,
    text='"Walnut and named confectionery produce eleven new products out of the world. Natural Delley Wesley, Walnut Fuel Diet, Coconut Oil and Grilled Glasses, are now 11 brand new, to choose a wide range of products after branded, it was officially released at the West Products Expo 2012, and will feature new discoveries over the coming months, including Almond Oil Cashew and Almond Cashew Oil, and Delicious White Extensions Chocolate Mini at 28 Walnut Oil. Call all nuts! Wesley Gold, co-founder of Wesley Gold, said: "I\'m very excited to introduce Walnut Oil Brass Products at Expo West." "We have given 11 new products, not just one, but also two new varieties of nuts, new flavors and new forms that differentiate between walnuts and sugar. Wait until you have a Maple Cashew taste. bones like my new favorite character! "', editor=lindsay)

    redone_fifteen_two = Edit(title='RIP Maggie', original=words_fifteen,
    text='Margaret, who has lived in the Hole community for a long time, died Wednesday, September 18, at the Sun Bridge Health Center. Ann In 1928 Hull, SD, Margaret received her Bachelor of Science in Nursing from Hull University Lace School in 1991. He resumed his education at Hull University, where he attended. Get your MD in Nursing in 1955. Margaret taught at Hull University in Amsterdam in the mid-1960s and worked in nursing homes throughout Massachusetts in the 1970s. He took a post as librarian at Hull County Technical School, where he worked until his retirement. Margaret loves good food and flowers, enjoys movies and games with friends, and has a big smile that can brighten a room. His father-in-law, Tablia Winslow and many of his grandparents, all living south of Hull, have been very happy in the years to come. Memorial gifts may be made to the human society of the Humpty Hole. Douglas, Hull\'s service was established.', editor=lindsay)

    redone_sixteen_two = Edit(title='We Think You WILL Like It!', original=words_sixteen, text='The theater people are pleased to announce Your Love Against the Background of New York City during the Great Depression. Conducting court-appointed opulence presentations for Hooverville of Arden, Rosalind, Orlando and their colleagues navigated estimates of love and class conditions in a military setting. Working words, music, and a pair of classic comics make it one of Shakespeares favorite comics.', editor=lindsay)

    redone_seventeen_two = Edit(title='Letter of Apology', original=words_seventeen,
    text='I feel you have a personal apology for the meeting yesterday. I know these days because I\'m sorry. I will be able to forgive me. I have great work honors together. I\'m very sorry.',
    editor=laura,
        liked_by=[anna, lindsay, ollie, alex, harry, laura],
        rating=15)

    redone_eighteen_two = Edit(title='Short Story About Stuff', original=words_eighteen,
    text='On the morning of June 27, it was clear and sunny, with the warmth of the whole summer; The flowers blossomed and the grass was green. Rural people began to gather about ten hours on the square between the post office and the bank; Many people in the city took the lottery for two days starting June 2. Only about three hundred people lived in the village, and the lottery took less than two hours, so it started at ten o\'clock in the morning and the villagers needed time to have dinner at home. After all, the boys met. The school was recently summer, and they often surrounded themselves with a sense of freedom, and gradually they quietly assembled for a while before the start of the game. And their speech was from the class and the teacher, books, and reprimands. Bobby Martin poured stones into his pockets, and the other boys chose the softest and roundest stones soon and followed his example; Bobby and Harry Jones and Dickey Delacroroy - the people of the village called the Dellacroi - eventually made a big pile in one corner of the square and protected the other children from aggression. The girls differed from each other, talked, looked at their shoulders, turned dust, or clung to their elder brothers. Soon people gathered. Talk about their children\'s survival, sowing and rains, tractors and taxes. They stood far away from the stones gathered around the corner, and instead of laughing, they were silent and smiling. Women wearing stale home dresses and sweatshirts came shortly after their own people.', editor=laura,
        liked_by=[anna, lindsay, ollie, alex, harry, laura],
        rating=15)

    redone_nineteen_two = Edit(title='Cover Letter', original=words_nineteen, text='I have a problem. See, my inbox currently (and embarrassingly) hosts 1,500 unread emails—including newsletters from at least 50 different brands. \n But this problem only fuels my passion for creating emails that are worth opening. Because from my perspective, as someone who can barely get through their own stack of mail, that’s a true win. \n \n I’ve been following Vitabe for years, and can proudly say that I open every single email you send to me. I’m a sucker for a good subject line—“Take a Vitamin-ute—We’ll A-B-C You Soon” being my favorite—and the way your email content feels both fun and expert-backed really speaks to me. This is why I’m thrilled to submit my application for a role as email marketing manager at your company. \n \n I have over four years of experience working in the email marketing space. In my current role at Westside Bank, I was able to implement new email campaigns centered around reengaging churned clients. By analyzing data around the types of clients who churn and the engagement of our current email subscribers, as well as A/B testing headlines and newsletter layouts, we were able to increase email subscribers by 15% and convert 30% of those subscribers to purchase our product, a significant increase from the previous year. I also launched a “Your Credit Matters” newsletter focused on educating our clients on how they spend and manage their credit—which became our highest performing campaign in terms of open-rates and click-through to date.', editor=laura)

    redone_twenty_two = Edit(title='HP FF', original=words_twenty, text='Albus moved under his blankets. His leg was torn off his plate (how did this happen?), And he sat in his bed, so that sunlight flowed through his window. She looked at art, who slept slowly in a sleeping bag on the floor. How did the person get the best sleep on earth? Albus felt sweaty and sad. His neck bent slightly. He must have laughed at her. Al up and down stairs, where mom and James ate breakfast. Her usual home is boring - she left yesterday Atlantis, after a day trip around the city. "I think Father and Lily are still sleeping?" Albus asked: He is tied up in the chair.  "Indeed, neither is Lily still asleep, but your father at work, the mother answered." But I thought Dad with us came to Diagon\'s Alley today! "It\'s their program they have two days in the World Cup, the next day It started on Diagon alley, and then art to school, but your father wanted to go with them on the Diagon , which was supposed to fall with us, but at an hour after this second morning, your father "What happened to you?" "What did he say to you?" James asked enthusiastically: "We do not say that they still do not know much. There was no strong evidence from this morning.""A strong certificate From what? " James asked, "Come on, mother, please?" Albus asked what was exciting to drag her father in the morning of her Diagon alley trip. Probably you will see the evening prophet tonight tonight. Oh, so, enough for the Prophet\'s version of the important era? "It\'s possible that the exciting news that was published during the day that the Prophet Muhammad was published the next morning," James excited. If not, surely it will be on the morning of the day. So you have to fill your breakfast today. Aunt Hermione, Rose, and Hugo in the liquid kettle this morning, right? about two hours, I think." Albus noted, they ate slowly for a few minutes. Albus left a glass of orange juice and wasted away from eating his own bread.', editor=laura,
        liked_by=[anna, lindsay, ollie, alex, harry, laura],
        rating=15)


    redone_one_three  = Edit(title='For You', original=words_one,
    text='I envy the small parts of the rock that surrounds you \n N around you \n what you offer \n" glittering elements \n "of women \n n without large quantities of luggage \n adhesives \n n before the thing that represents the place.I grew up on the soft fingers of the gods and small mammals Tears and tears, I realized what flowers seem to be not today means that \n NI have manufactured this poem by HIMSELF and have not lost it (yet)',
    editor=alex,
        liked_by=[anna, lindsay, ollie, alex, harry, laura],
        rating=15)
    redone_two_three = Edit(title='Making A Very Excellent Formal Complaint to BA', original=words_two,
    text='Who is to be touched by this, I wrote to some on April 19, 1919, after a two-way trip from Cape Town to London Heathrow. As you know, on-board entertainment completely fails in 11 hours. Our staff was stubborn and extremely compelling during the trip, which made it very unpopular. The hotel is north of BA 20 LE per vote. After a live performance, we found out that the entertainment system on the board didn\'t work. We did not start, but the cockpit staff told us that it was possible to restart the system after Greg Underview, a customer communications manager, told them that the system was not working. After trying for three to 45 minutes without restoration, I heard what a lot of passengers should do with this crew. They have experienced vampire confusion, frustration and self-defense in our wardrobe, especially in Medellia and Philip. I heard informing passengers that the situation was described as "unfair" and that they left without apology. Each staff member left the case for more than two hours and was never found. Finally, Greg spoke to each of the affected passengers and apologized for the problem. I told her we felt the staff situation was rejected and that they were probably apologizing. We received a complaint message and were told that we would receive compensation. I would like to say that while talking to the passenger on the occasion, who was on BA\'s 11th flight with a broken screen, it was admitted that the aircraft was "very old" and the screen was "everywhere", When it was astonished that the British Airways Company had deliberately allowed passengers to use it. Their money is on seats that were not available. We provide basic facilities. In addition to the broken screen during the 11-hour flight, the staff was stubborn and unhappy when they returned to the ship, picking up passengers and forcing us to meet basic needs, such as alcohol. General Chat Chat Lounge At the end of the trip, Matilda served guests quite a bit. However, some lines were closed in front of us and they were gone. Then Philip brought some tea. The passengers were quite comfortable, and Philip replied, "I made no suggestions to find the staff\'s fault or to apologize." Also, during the flight, I heard another sad passenger about food. It was a bad experience from start to finish and £ 20 on a large scale is needed to pay for them.',
    editor=anna,
        liked_by=[anna, lindsay, ollie, alex, harry, laura],
        rating=19)
    redone_three_three  = Edit(title='Bar Job Cover Letter', original=words_three,
    text='Dear Ms. Applebee: \n When I learned of your need for a new member to join your bar staff team, I hasted to send you my resume for your consideration. With key experience providing excellent customer service in both casual and fine dining establishments—as well as my commitment to dynamic team collaboration and leadership—I would significantly benefit McIntyre Bar & Grill in this role. \n My experience in preparing and delivering cocktails, beer, wine, and spirits for diverse clientele has prepared me to excel in this role. Complementing this expertise is my proficiency in order taking, table setting, stock management, and premises maintenance. With my proven ability to create sophisticated alcoholic and non-alcoholic beverages while maintaining a clean and safe environment, my additional strengths in communication and time management position me to thrive in this position. \n \n Highlights of my background include: \n \n Greeting bar guests and taking orders, delivering accurate food and beverage items, collecting and processing payments, maintaining optimal inventory levels, and balancing multiple tasks simultaneously in fast-paced restaurants. \n Providing overarching support to bar managers with a full range of operational tasks to achieve top levels of efficiency and customer satisfaction. \n Demonstrating team building and organizational planning abilities, strong leadership talents, and exceptional interpersonal skills; mentoring new staff in general bar and restaurant operations. \n With my previous experience, coupled with my enthusiasm and my personable, outgoing demeanor, I could swiftly surpass your expectations for this role. I look forward to discussing the position in further detail. Thank you for your consideration. \n \n Sincerely, \n \n Hamish Horesdale',
    editor=alex)
    redone_four_three = Edit(title='Thanks for coming to our big day, loved the money!', original=words_four,
    text='We are so so so so so full of thank you for celebrating our massive twenty four hours in combination with us, which made it one of the most memorable days in your life. During the event, I danced all day in the rain, jumped together and felt the day of love. We can not wait to go to Europe at the end of July, it will not happen without all the good gifts. We look forward to the next chapter of our life and share with you new memories! "',
    editor=harry,
        liked_by=[anna, laura],
        rating=9)
    redone_five_three  = Edit(title='Valentine', original=words_five,
    text='If you were my rose, then I\'d be your sun, \n painting you rainbows when the rains come. \n I\'d change my orbit to banish the night, \n as to keep you in my nurturing light. \n \n If you were my world, then I\'d be your moon, \n your silent protector, a night-light in the gloom. \n Our fates intertwined, two bodies in motion \n through time and space, our dance of devotion. \n \n If you were my island, then I\'d be your sea, \n caressing your shores, soft and gentle I\'d be. My tidal embrace would leave gifts on your sands, \n but by current and storm, I\'d ward your gentle lands. \n \n If you were love\'s promise, then I would be time, \n your constant companion till stars align. \n And though we are mere mortals, true love is divine, \n and my devotion eternal, to my one valentine. ',
    editor=harry,
        liked_by=[anna, laura],
        rating=7)
    redone_six_three  = Edit(title='Hire Me and I will assist YOU!', original=words_six,
    text='Dear Felix, On behalf of my representative, I love your work and I believe in your skills and abilities to help you finish it. When a service is issued, the President of the company expresses his need to assist him in both aspects of the project. My current role as auxiliary support. I am a key player between my team and team so that I can focus on minimizing activities my chance to reduce self and reduce my choices. To continue this activity, you will learn to benefit others. Wechsler 7% class. It also uses direct connection with meetings, meetings, and preparation of papa. This file is recommended for advisory plans when discouraged. Thank you for reviewing your application. This is Elena Biszorp',
    editor=harry,
        liked_by=[anna, lindsay, ollie, alex, harry, laura],
        rating=14)
    redone_seven_three = Edit(title='Personal Brand Statement', original=words_seven,
    text='A focused and determined business leader, I offer the entrepreneurial stamina and wisdom to drive bottom line growth and lucrative business, inspire employees to peak performance, and cultivate profitable business relationships built on respect, loyalty, and trust. My easy-going sense of humor has been a defining management strategy to bring out the best in everyone, instill pride, and mobilize them to make their company the best in the industry.',
    editor=lindsay,
        liked_by=[anna, lindsay, ollie, alex, harry, laura],
        rating=14)
    redone_eight_three = Edit(title='Fast Food Complain', original=words_eight,
    text='I visited an anonymous restaurant at 341 Hampton Rd. Friday, June 6. We arrived at 11.45. Please provide me with a copy of the invoice for your convenience. This is the nearest office. We met at least five times last year. Our Friday experience was a no brainer. We are not satisfied with chastity and curiosity. All the garbage tables are dirty and full of junk and junk. In addition, the house cleans the floor. The bathroom is not very clean. Previously, the restaurant was clean. We enjoyed Taco\'s joy. If improvements are made, we may meet in the future. We usually visit at least once a month. Hide me. Thanks for the answer. Hi to you, William McPurry',
    editor=lindsay,
        liked_by=[anna, lindsay, ollie, alex, harry, laura],
        rating=19)
    redone_nine_three = Edit(title='Dance Teach CL', original=words_nine,
    text='My inspiration for dance lessons came from the same effect that led me to my dance career nearly 13 years ago." Since the onset of my education in the arts, I have tried to use the language of the body to tell stories And feeling in the new language, and I became a strong supporter of teaching others. Throughout my career, I have seen dancing One to increase the life of dance and drama, and as my dad, I see students learn different kinds of dance and follow their creative expression, believe in encouragement. Dancing is the first experience to develop the perspective of people who are interested in creating their own experience of creative, creative and creative. Believe me. Attempting my experience is related to ... A group of dancers aged 4 to 14 years old as a young dancer, Beck Cred studio studio. Dance and activities make the students happy and happy. Introduce tips, music and music for students to experience.  In giving information about the dance style Adults with a fascinating story and discussion by using various teaching methods for each group. Manage different administrative tasks, including parental, scheduling, and payment communications. I got my MFA to dance at the MFA College and an introductory level in Natural Dance as a graduate assistant. San Francisco Spark Temp has been working for 13 years as a painter, artist, journalist and guest speaker (for a complete list of testimonials and art available upon request). My deep experience as a professional dancer and to inspire new and varied singers, I have successfully delivered Chrysalis Dance. I look forward to discussing my position and my advantages. Thanks for your attention. \n \n Sincerely, \n  nMartha Green Park',
    editor=harry,
        liked_by=[anna, lindsay, ollie, alex, harry, laura],
        rating=19)
    redone_ten_three = Edit(title='No, Cadbury\'s No.', original=words_ten,
    text='"I do not want to believe that the last chocolate bar has a different taste, so it\'s different, so I look online to see how other people have had a lot of negative analyzes after changing the same formula. Years and have used Cadbury, I\'m not interested! I have a little pie for a cup ... I will not buy another brand from now on to find D The correct formula is no different, and it does not break with the dark chocolate.',
    editor=harry,
        liked_by=[anna, lindsay, ollie, alex, harry, laura],
        rating=7)
    redone_eleven_three = Edit(title='Complaint to Restaurant', original=words_eleven,
    text='Dear Sir, I went to your restaurant on September 10, 2013 for dinner with your family.  He reported it to his supervisor, but he declined our comment and was horrified when he asked us to find another restaurant. \n \n The children started complaining about the discomfort and we took them to a hospital. Doctors declared food poisoning. Timely medical care can prevent serious harm. \n \n I urge you to take action against the service officers. I will send a copy of the hospital bill for a refund to take the case to the Consumer Forum to take strict action against your restaurant. \n \n Thanks, \n \n Graham Short',
    editor=lindsay,
        liked_by=[anna, lindsay, ollie, alex, harry, laura],
        rating=7)
    redone_twelve_three  = Edit(title='Junior Web Developer Cover Letter', original=words_twelve,
    text='Dear Mr. Martinez, \n \n I read with enthusiasm your recent advertisement for the Junior Web Developer position and am writing to express my interest. My superior focus and attention to detail combined with my extensive knowledge of HTML Javascript XML and SQL/PLSQL makes me an exceptional choice. \n \n In my current role as a Junior Web Developer I have developed web-based applications from design to coding and full implementation under the direction of the Senior Developer. By relying on solid programming knowledge as well as excellent oral and verbal communication I have consistently produced terrific code within customer-set deliverables time frames. Due to my diligence and hard work I have been awarded regular promotions and bonuses as a result. I bring a Bachelor’s Degree in Information Technology along with regular updates and certifications. My abilities to produce excellent code and to clearly communicate and collaborate with coworkers customers and management have led to company successes. I have five years of Junior Web Developer experience and am committed to staying up-to-date with all technological advancements. All of my qualifications make me an exceptional candidate for the Junior Web Developer position. \n \n Please call to schedule an interview. I have enclosed my resume and look forward to meeting. \n \n  Sincerely, \n \n Fiona Brackensmist Hadden',
    editor=anna,
        liked_by=[anna, lindsay, ollie, alex, harry, laura],
        rating=7)


    redone_thirteen_three  = Edit(title='Start-Up Press Release', original=words_fourteen,
    text='I want to meet someone to practice English with me, right now I have a very good experience!',
    editor=anna,
        liked_by=[anna, lindsay, ollie, alex, harry, laura],
        rating=7)

    redone_fourteen_three  = Edit(title='GO NUTS FOR NUTS (in the form of butter)!', original=words_fourteen,
    text='Named Nuts and Confectionery producing eleven new products from around the world, Natural Delley Wesley, Walnut Fuel Diet, Coconut Oil and Grilled Glasses, are 11 new to choose from. a wide range of branded products, has been officially launched at the West Products Expo 2012 and will feature new discoveries in the coming months, including almond cashew and cashew oil and the tiny white chocolate Delicious Extension 28 Nut Oil Call All Nuts Wesley Gold, co-founder of Wesley Gold, said: "I am very excited to introduce Walnut Oil Brass Products at the West Expo." "We\'ve given 11 new products, not just one, but also two new nut varieties, new flavors, and new shapes that distinguish between nuts and sugar. Wait until you get a Maphe Cashew flavor. Bones as my new favorite character!"', editor=lindsay,
        liked_by=[anna, lindsay, ollie, alex, harry, laura],
        rating=7)

    redone_fifteen_three  = Edit(title='May Margaret Rest In peaceful Slumber', original=words_fifteen,
    text='Ms Margaret, who has lived in the Hull community for a long time, passed away on Wednesday, January 18 at the Sun Bridge Health Center. In 1928 Hull, SD, Margaret accepted her Bachelor of Science in Nursing from Hull University High School in 1991. He resumed his education at Hull University, where he attended. Get your MD in Nursing in 1955. Margaret taught at Hull University in Amsterdam in the mid-1960s and worked in nursing homes in Massachusetts in the 1970s. He took a post as librarian at Hull County Technical School, where he worked until his retirement. Margaret loves good food and flowers, enjoys movies and games with friends, and has a big smile that can shine in a room. Her in-laws, Tablia Winslow and many of her grandparents, all living south of Hull, are delighted in the years to come. Memories can be gifted in human society at the Empty Hole. Douglas service, Hole was established.', editor=lindsay,
        liked_by=[anna, laura],
        rating=4)

    redone_sixteen_three  = Edit(title='We Think You WILL Like It!', original=words_sixteen, text='The theater people are proud to announce Your Love Against the Background of New York City during the Great Depression. He held court-appointed discontent presentations for Hooverville from Arden, Rosalind, Orlando and their colleagues steering estimates of love and class conditions in a military location. Working words, music, and a pair of classical comics make it one of Shakespeare\'s favourite comics', editor=lindsay)

    redone_seventeen_three = Edit(title='Letter of Apology', original=words_seventeen,
    text='I feel you really really deserve a MASSIVE MASSIVE SORRY! A personal proper apology for the meeting yesterday. I know these days because I\'m sorry. I hope you will be able to forgive me. I have great work honor to work together with you. I\'m very sorry. Please please forgive me.... ',
    editor=laura,
        liked_by=[anna, lindsay, ollie, alex, harry, laura],
        rating=4)

    redone_eighteen_three = Edit(title='Story SHORt', original=words_eighteen,
    text='On the morning of June 27, the heat was clear all summer. Too much piece and green grass. The man stopped for ten minutes at the post office and the bank. Many people started working in the city on June 2 for two days. There were only three hundred people living in rural areas and the crisis went down for two hours, so that the morning started at ten and the villagers needed food. After the chat boy. It was a summer school and often surrounded his independence and quickly started working. And lectures on class and teacher, books and titles. Bobby Martin picked up his stones and quickly and easily received other children to get the most beautiful and bright stones. Bobby and Harry Jones and Dickie Dellcrovey - people in the village say - have finally been built in forest areas and other children protected by the ceasefire. Boys are different, talking, looking at their stones, stealing or becoming strangers to their ancestors. Talk about kids, forests and mountains, tractors and tax collection early. They stood around the rock, gathered around the boat, replaced instead, were quiet and quiet. Women\'s clothing and bedding are near their time.', editor=laura,
        liked_by=[anna, lindsay, ollie, alex, harry, laura],
        rating=4)

    redone_nineteen_three = Edit(title='Letter of Cover', original=words_sixteen, text='I have difficulty seeing that my inbox (and embarrassment) keeps 1,500 emails unread - including newsletters from at least 50 different species. n But this problem just makes me create emails worth the opening. From my point of view, using his job is a real benefit.  I\'ve been following Vitabe for many years and I can say that I will open any email you send to me. I have a nice cube for a good subject line - "Check out vitamin-ute - our favorite thing comes from ABC" is my favorite - and how your email content feels fun and specialist support, talking to me. For this reason, I am pleased to present my application for the position of marketing manager for email in your company. I have four years of experience in email marketing. My current role at West Side Bank was possible to run new email initiatives that were enforced on customers. By analyzing data on the different types of customers that are changing and interacting with the people currently receiving money, in addition to the A / B exam results and the touring drawings. letters, we managed to charge the fees by 15% and 30% of these subscribers In order to buy our result, a significant increase from the previous year. I also focused on the Credit Matters newsletter to educate our customers on how they spend and manage their credit, which is the highest level of open recordings which they hold. clicks.', editor=laura,
        liked_by=[anna, lindsay, ollie, alex, harry, laura],
        rating=4)

    redone_twenty_three = Edit(title='Press Release for Production of As You Like It', original=words_twenty, text='Albus moved under his blankets. His leg was torn off his plate (how did this happen?), And he sat in his bed, so that sunlight flowed through his window. She looked at art, who slept slowly in a sleeping bag on the floor. How did the person get the best sleep on earth? Albus felt sweaty and sad. His neck bent slightly. He must have laughed at her. Al up and down stairs, where mom and James ate breakfast. Her usual home is boring - she left yesterday Atlantis, after a day trip around the city. "I think Father and Lily are still sleeping?" Albus asked: He is tied up in the chair.  "Indeed, neither is Lily still asleep, but your father at work, the mother answered." But I thought Dad with us came to Diagon\'s Alley today! "It\'s their program they have two days in the World Cup, the next day It started on Diagon alley, and then art to school, but your Dad wanted to go with them on the Diagon , which was supposed to fall with us, but at an hour after this second morning, your father "What happened to you?" "What did he say to you?" James asked enthusiastically: "We do not say that they still do not know much. There was no strong evidence from this morning.""A strong certificate From what? " James asked, "Come on, mother, please?" Albus asked what was exciting to drag her father in the morning of her Diagon alley trip. Probably you will see the evening prophet tonight tonight. Oh, so, enough for the Prophet\'s version of the important era? "It\'s possible that the exciting news that was published during the day that the Prophet Muhammad was published the next morning," James excited. Otherwise, surely it will be on the morning of the day. So you have to fill your breakfast today. Aunt Hermione, Rose, and Hugo in the liquid kettle this morning, right? about two hours, I think." Albus noted, they ate slowly for a few minutes. Albus left a glass of orange juice and wasted away from eating his own bread.', editor=laura,
        liked_by=[anna, lindsay, ollie, alex, harry, laura],
        rating=4)

    final_sixteen = Final(edit=edited_sixteen)
    final_fifteen = Final(edit=edited_fifteen_two)
    final_fourteen = Final(edit=edited_fourteen_two)


    db.session.add(lily)
    db.session.add(lindsay)
    db.session.add(anna)
    db.session.add(harry)
    db.session.add(laura)
    db.session.add(alex)
    db.session.add(ollie)


    db.session.add(wes)
    db.session.add(sheema)
    db.session.add(shane)
    db.session.add(talha)
    db.session.add(cliff)
    db.session.add(mia)
    db.session.add(sim)
    db.session.add(amy)
    db.session.add(tom)
    db.session.add(cliff)
    db.session.add(mia)
    db.session.add(sim)
    db.session.add(daniela)
    db.session.add(charlie)
    db.session.add(daniela)
    db.session.add(jack)

    db.session.add(work)
    db.session.add(formal)
    db.session.add(business)
    db.session.add(personal)
    db.session.add(poetry)
    db.session.add(prose)
    db.session.add(formal_communications)
    db.session.add(complaint)
    db.session.add(cover_letter)
    db.session.add(CV)
    db.session.add(romance)
    db.session.add(enquiry)
    db.session.add(suggestion)
    db.session.add(criticism)
    db.session.add(journalism)
    db.session.add(blog)
    db.session.add(short_story)
    db.session.add(fan_fiction)
    db.session.add(family)
    db.session.add(thank_you)
    db.session.add(appreciation)
    db.session.add(family)
    db.session.add(feedback)
    db.session.add(application)
    db.session.add(obituary)
    db.session.add(branding)
    db.session.add(press_release)
    db.session.add(request)
    db.session.add(language)
    db.session.add(education)
    db.session.add(apology)

    db.session.add(writing_one)
    db.session.add(writing_two)
    db.session.add(writing_three)
    db.session.add(writing_four)
    db.session.add(writing_five)
    db.session.add(writing_six)
    db.session.add(writing_seven)
    db.session.add(writing_eight)
    db.session.add(writing_nine)
    db.session.add(writing_ten)
    db.session.add(writing_eleven)
    db.session.add(writing_twelve)
    db.session.add(writing_thirteen)
    db.session.add(writing_fourteen)
    db.session.add(writing_fifteen)
    db.session.add(writing_sixteen)
    db.session.add(writing_seventeen)
    db.session.add(writing_eighteen)
    db.session.add(writing_nineteen)
    db.session.add(writing_twenty)


    db.session.add(edited_one)
    db.session.add(edited_two)
    db.session.add(edited_three)
    db.session.add(edited_four)
    db.session.add(edited_five)
    db.session.add(edited_six)
    db.session.add(edited_seven)
    db.session.add(edited_eight)
    db.session.add(edited_nine)
    db.session.add(edited_ten)
    db.session.add(edited_eleven)
    db.session.add(edited_twelve)
    db.session.add(edited_thirteen)
    db.session.add(edited_fourteen)
    db.session.add(edited_fifteen)
    db.session.add(edited_sixteen)
    db.session.add(edited_seventeen)
    db.session.add(edited_eighteen)
    db.session.add(edited_nineteen)
    db.session.add(edited_twenty)

    db.session.add(edited_one_two)
    db.session.add(edited_two_two)
    db.session.add(edited_three_two)
    db.session.add(edited_four_two)
    db.session.add(edited_five_two)
    db.session.add(edited_six_two)
    db.session.add(edited_seven_two)
    db.session.add(edited_eight_two)
    db.session.add(edited_nine_two)
    db.session.add(edited_ten_two)
    db.session.add(edited_eleven_two)
    db.session.add(edited_twelve_two)
    db.session.add(edited_thirteen_two)
    db.session.add(edited_fourteen_two)
    db.session.add(edited_fifteen_two)
    db.session.add(edited_sixteen_two)
    db.session.add(edited_seventeen_two)
    db.session.add(edited_eighteen_two)
    db.session.add(edited_nineteen_two)
    db.session.add(edited_twenty_two)

    db.session.add(edited_one_three)
    db.session.add(edited_three)
    db.session.add(edited_three_three)
    db.session.add(edited_four_three)
    db.session.add(edited_five_three)
    db.session.add(edited_six_three)
    db.session.add(edited_seven_three)
    db.session.add(edited_eight_three)
    db.session.add(edited_nine_three)
    db.session.add(edited_ten_three)
    db.session.add(edited_eleven_three)
    db.session.add(edited_twelve_three)
    db.session.add(edited_thirteen_three)
    db.session.add(edited_fourteen_three)
    db.session.add(edited_fifteen_three)
    db.session.add(edited_sixteen_three)
    db.session.add(edited_seventeen_three)
    db.session.add(edited_eighteen_three)
    db.session.add(edited_nineteen_three)
    db.session.add(edited_twenty_three)

    db.session.add(words_one)
    db.session.add(words_two)
    db.session.add(words_three)
    db.session.add(words_four)
    db.session.add(words_five)
    db.session.add(words_six)
    db.session.add(words_seven)
    db.session.add(words_eight)
    db.session.add(words_nine)
    db.session.add(words_ten)
    db.session.add(words_eleven)
    db.session.add(words_twelve)
    db.session.add(words_thirteen)
    db.session.add(words_fourteen)
    db.session.add(words_fifteen)
    db.session.add(words_sixteen)
    db.session.add(words_seventeen)
    db.session.add(words_eighteen)
    db.session.add(words_nineteen)
    db.session.add(words_twenty)


    db.session.add(redone_one)
    db.session.add(redone_two)
    db.session.add(redone_three)
    db.session.add(redone_four)
    db.session.add(redone_five)
    db.session.add(redone_six)
    db.session.add(redone_seven)
    db.session.add(redone_eight)
    db.session.add(redone_nine)
    db.session.add(redone_ten)
    db.session.add(redone_eleven)
    db.session.add(redone_twelve)
    db.session.add(redone_thirteen)
    db.session.add(redone_fourteen)
    db.session.add(redone_fifteen)
    db.session.add(redone_sixteen)
    db.session.add(redone_seventeen)
    db.session.add(redone_eighteen)
    db.session.add(redone_nineteen)
    db.session.add(redone_twenty)

    db.session.add(redone_one_two)
    db.session.add(redone_two_two)
    db.session.add(redone_three_two)
    db.session.add(redone_four_two)
    db.session.add(redone_five_two)
    db.session.add(redone_six_two)
    db.session.add(redone_seven_two)
    db.session.add(redone_eight_two)
    db.session.add(redone_nine_two)
    db.session.add(redone_ten_two)
    db.session.add(redone_eleven_two)
    db.session.add(redone_twelve_two)
    db.session.add(redone_thirteen_two)
    db.session.add(redone_fourteen_two)
    db.session.add(redone_fifteen_two)
    db.session.add(redone_sixteen_two)
    db.session.add(redone_seventeen_two)
    db.session.add(redone_eighteen_two)
    db.session.add(redone_nineteen_two)
    db.session.add(redone_twenty_two)

    db.session.add(redone_one_three)
    db.session.add(redone_three)
    db.session.add(redone_three_three)
    db.session.add(redone_four_three)
    db.session.add(redone_five_three)
    db.session.add(redone_six_three)
    db.session.add(redone_seven_three)
    db.session.add(redone_eight_three)
    db.session.add(redone_nine_three)
    db.session.add(redone_ten_three)
    db.session.add(redone_eleven_three)
    db.session.add(redone_twelve_three)
    db.session.add(redone_thirteen_three)
    db.session.add(redone_fourteen_three)
    db.session.add(redone_fifteen_three)
    db.session.add(redone_sixteen_three)
    db.session.add(redone_seventeen_three)
    db.session.add(redone_eighteen_three)
    db.session.add(redone_nineteen_three)
    db.session.add(redone_twenty_three)


    db.session.commit()
