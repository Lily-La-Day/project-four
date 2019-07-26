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

    lily, errors = writer_schema.load({
        'username': 'lily',
        'email': 'lily@email',
        'password': 'pass',
        'password_confirmation': 'pass'
    })

    if errors:
        raise Exception(errors)

    laila, errors = editor_schema.load({
            'username': 'laila',
            'email': 'laila@email',
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

    if errors:
        raise Exception(errors)

    writing_one = Writing(
    title='For You',
    text='This letter describes the action taken regarding complaints of sexual harassment against John Doe. Mr. Doe was notified by letter of the complaints, and he met with me April 12 for further discussion of the matter. We reviewed the specific nature of each complaint originating in the accounting department and carefully examined company policy on each issue. Mr. Doe was informed that his employment with Doe Corporation would be terminated if more substantiated complaints of this nature were received. He has agreed to attend classes given by the human resources department to help him be more aware of the types of behaviors that may be offensive to others.',
    categories=[romance, personal],
    author=lily
    )
    writing_two = Writing(
    title='British Airways Complaint',
    text='This letter describes the action taken regarding complaints of sexual harassment against John Doe. Mr. Doe was notified by letter of the complaints, and he met with me April 12 for further discussion of the matter. We reviewed the specific nature of each complaint originating in the accounting department and carefully examined company policy on each issue. Mr. Doe was informed that his employment with Doe Corporation would be terminated if more substantiated complaints of this nature were received. He has agreed to attend classes given by the human resources department to help him be more aware of the types of behaviors that may be offensive to others.',
    categories=[business, formal, complaint],
    author=lily
    )
    writing_three = Writing(
    title='Bar Job Cover Letter',
    text='This letter describes the action taken regarding complaints of sexual harassment against John Doe. Mr. Doe was notified by letter of the complaints, and he met with me April 12 for further discussion of the matter. We reviewed the specific nature of each complaint originating in the accounting department and carefully examined company policy on each issue. Mr. Doe was informed that his employment with Doe Corporation would be terminated if more substantiated complaints of this nature were received. He has agreed to attend classes given by the human resources department to help him be more aware of the types of behaviors that may be offensive to others.',
    categories=[work, cover_letter, CV],
    author=lily
    )
    writing_four = Writing(
    title='Wedding Thank You',
    text='This letter describes the action taken regarding complaints of sexual harassment against John Doe. Mr. Doe was notified by letter of the complaints, and he met with me April 12 for further discussion of the matter. We reviewed the specific nature of each complaint originating in the accounting department and carefully examined company policy on each issue. Mr. Doe was informed that his employment with Doe Corporation would be terminated if more substantiated complaints of this nature were received. He has agreed to attend classes given by the human resources department to help him be more aware of the types of behaviors that may be offensive to others.',
    categories=[personal, family, thank_you],
    author=lily
    )
    writing_five = Writing(
    title='Valentines Poem',
    text='This letter describes the action taken regarding complaints of sexual harassment against John Doe. Mr. Doe was notified by letter of the complaints, and he met with me April 12 for further discussion of the matter. We reviewed the specific nature of each complaint originating in the accounting department and carefully examined company policy on each issue. Mr. Doe was informed that his employment with Doe Corporation would be terminated if more substantiated complaints of this nature were received. He has agreed to attend classes given by the human resources department to help him be more aware of the types of behaviors that may be offensive to others.',
    categories=[romance, personal],
    author=lily
    )
    writing_six = Writing(
    title='PA Application',
    text='This letter describes the action taken regarding complaints of sexual harassment against John Doe. Mr. Doe was notified by letter of the complaints, and he met with me April 12 for further discussion of the matter. We reviewed the specific nature of each complaint originating in the accounting department and carefully examined company policy on each issue. Mr. Doe was informed that his employment with Doe Corporation would be terminated if more substantiated complaints of this nature were received. He has agreed to attend classes given by the human resources department to help him be more aware of the types of behaviors that may be offensive to others.',
    categories=[work, business, CV, cover_letter],
    author=lily
    )
    writing_seven = Writing(
    title='Brand Statement',
    text='This letter describes the action taken regarding complaints of sexual harassment against John Doe. Mr. Doe was notified by letter of the complaints, and he met with me April 12 for further discussion of the matter. We reviewed the specific nature of each complaint originating in the accounting department and carefully examined company policy on each issue. Mr. Doe was informed that his employment with Doe Corporation would be terminated if more substantiated complaints of this nature were received. He has agreed to attend classes given by the human resources department to help him be more aware of the types of behaviors that may be offensive to others.',
    categories=[business, formal, work],
    author=lily
    )
    writing_eight = Writing(
    title='Pret-A-Manger Complaint',
    text='This letter describes the action taken regarding complaints of sexual harassment against John Doe. Mr. Doe was notified by letter of the complaints, and he met with me April 12 for further discussion of the matter. We reviewed the specific nature of each complaint originating in the accounting department and carefully examined company policy on each issue. Mr. Doe was informed that his employment with Doe Corporation would be terminated if more substantiated complaints of this nature were received. He has agreed to attend classes given by the human resources department to help him be more aware of the types of behaviors that may be offensive to others.',
    categories=[complaint, formal],
    author=lily
    )
    writing_nine = Writing(
    title='Dance Teacher Cover Letter',
    text='This letter describes the action taken regarding complaints of sexual harassment against John Doe. Mr. Doe was notified by letter of the complaints, and he met with me April 12 for further discussion of the matter. We reviewed the specific nature of each complaint originating in the accounting department and carefully examined company policy on each issue. Mr. Doe was informed that his employment with Doe Corporation would be terminated if more substantiated complaints of this nature were received. He has agreed to attend classes given by the human resources department to help him be more aware of the types of behaviors that may be offensive to others.',
    categories=[work, CV, application],
    author=lily
    )
    writing_ten = Writing(
    title='Cadburys New Recipe Feedback',
    text='This letter describes the action taken regarding complaints of sexual harassment against John Doe. Mr. Doe was notified by letter of the complaints, and he met with me April 12 for further discussion of the matter. We reviewed the specific nature of each complaint originating in the accounting department and carefully examined company policy on each issue. Mr. Doe was informed that his employment with Doe Corporation would be terminated if more substantiated complaints of this nature were received. He has agreed to attend classes given by the human resources department to help him be more aware of the types of behaviors that may be offensive to others.',
    categories=[formal, feedback],
    author=lily
    )
    writing_eleven = Writing(
    title='Waiter Misconduct Complaint',
    text='This letter describes the action taken regarding complaints of sexual harassment against John Doe. Mr. Doe was notified by letter of the complaints, and he met with me April 12 for further discussion of the matter. We reviewed the specific nature of each complaint originating in the accounting department and carefully examined company policy on each issue. Mr. Doe was informed that his employment with Doe Corporation would be terminated if more substantiated complaints of this nature were received. He has agreed to attend classes given by the human resources department to help him be more aware of the types of behaviors that may be offensive to others.',
    categories=[formal, feedback, complaint],
    author=lily
    )
    writing_twelve = Writing(
    title='Junior Web Developer Cover Letter',
    text='This letter describes the action taken regarding complaints of sexual harassment against John Doe. Mr. Doe was notified by letter of the complaints, and he met with me April 12 for further discussion of the matter. We reviewed the specific nature of each complaint originating in the accounting department and carefully examined company policy on each issue. Mr. Doe was informed that his employment with Doe Corporation would be terminated if more substantiated complaints of this nature were received. He has agreed to attend classes given by the human resources department to help him be more aware of the types of behaviors that may be offensive to others.',
    categories=[work, application, business, CV],
    author=lily
    )
    writing_thirteen = Writing(
    title='English Practiss',
    text='This letter describes the action taken regarding complaints of sexual harassment against John Doe. Mr. Doe was notified by letter of the complaints, and he met with me April 12 for further discussion of the matter. We reviewed the specific nature of each complaint originating in the accounting department and carefully examined company policy on each issue. Mr. Doe was informed that his employment with Doe Corporation would be terminated if more substantiated complaints of this nature were received. He has agreed to attend classes given by the human resources department to help him be more aware of the types of behaviors that may be offensive to others.',
    categories=[prose, short_story],
    author=lily
    )
    writing_fourteen = Writing(
    title='MY STARTUP!!!!!!',
    text='This letter describes the action taken regarding complaints of sexual harassment against John Doe. Mr. Doe was notified by letter of the complaints, and he met with me April 12 for further discussion of the matter. We reviewed the specific nature of each complaint originating in the accounting department and carefully examined company policy on each issue. Mr. Doe was informed that his employment with Doe Corporation would be terminated if more substantiated complaints of this nature were received. He has agreed to attend classes given by the human resources department to help him be more aware of the types of behaviors that may be offensive to others.',
    categories=[business, formal],
    author=lily
    )
    writing_fifteen = Writing(
    title='Grannys Obitchuary',
    text='This letter describes the action taken regarding complaints of sexual harassment against John Doe. Mr. Doe was notified by letter of the complaints, and he met with me April 12 for further discussion of the matter. We reviewed the specific nature of each complaint originating in the accounting department and carefully examined company policy on each issue. Mr. Doe was informed that his employment with Doe Corporation would be terminated if more substantiated complaints of this nature were received. He has agreed to attend classes given by the human resources department to help him be more aware of the types of behaviors that may be offensive to others.',
    categories=[personal, formal, obituary, journalism],
    author=lily
    )

    writing_sixteen = Writing(
    title='news paper artical for advertising as you like it',
    text='This letter describes the action taken regarding complaints of sexual harassment against John Doe. Mr. Doe was notified by letter of the complaints, and he met with me April 12 for further discussion of the matter. We reviewed the specific nature of each complaint originating in the accounting department and carefully examined company policy on each issue. Mr. Doe was informed that his employment with Doe Corporation would be terminated if more substantiated complaints of this nature were received. He has agreed to attend classes given by the human resources department to help him be more aware of the types of behaviors that may be offensive to others.',
    categories=[journalism, ],
    author=lily
    )

    edited_fourteen = Edit(title='Start-Up Press Release', original=writing_fourteen,
    text='He is a very compotent coder who rarely uses Google and watches Netflix at the weekend',
    editor=laila)

    edited_fifteen = Edit(title='Margaret Deedward\'s Obituary', original=writing_fifteen,
     text='He owns a cat called Cheeseburger and quite frequently refers to a dream of working for MindGeek', editor=laila)

    edited_sixteen = Edit(title='Press Release for Production of As You Like It', original=writing_sixteen, text='He is a very nice young man', editor=laila)

    edited_fourteen_two = Edit(title='New Nut Butter Brand Is Answer To Your Nutty Prayers!', original=writing_fourteen,
     text='He does some stuff well in  code land and he is one whom rarely uses Google and watches the television box', editor=lindsay)

    edited_fifteen_two = Edit(title='RIP Maggie', original=writing_fifteen,
    text='He is a master of felines and a cat called Cheeseburger and is fan of MindGeek', editor=lindsay)

    edited_sixteen_two = Edit(title='We Think You WILL Like It!', original=writing_sixteen, text='WE LIKE HIM COS He is a very nice young man', editor=lindsay)

    final_sixteen = Final(edit=edited_sixteen)
    final_fifteen = Final(edit=edited_fifteen_two)
    final_fourteen = Final(edit=edited_fourteen_two)


    db.session.add(lily)
    db.session.add(laila)
    db.session.add(lindsay)

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

    db.session.add(writing_one)
    db.session.add(writing_one)
    db.session.add(writing_one)
    db.session.add(writing_one)
    db.session.add(writing_one)
    db.session.add(writing_one)
    db.session.add(writing_one)
    db.session.add(writing_one)
    db.session.add(writing_one)
    db.session.add(writing_one)
    db.session.add(writing_one)
    db.session.add(writing_one)
    db.session.add(writing_one)
    db.session.add(writing_one)
    db.session.add(writing_one)
    db.session.add(writing_one)
    db.session.add(writing_one)
    db.session.add(edited_fourteen)
    db.session.add(edited_fifteen)
    db.session.add(edited_sixteen)
    db.session.add(edited_fourteen_two)
    db.session.add(edited_fifteen_two)
    db.session.add(edited_sixteen_two)

    db.session.commit()
