from app import app, db
from models.writing import Writing
from models.edit import Edit
from models.writer import WriterSchema
from models.editor import EditorSchema

writer_schema = WriterSchema()
editor_schema = EditorSchema()

with app.app_context():
    db.drop_all()
    db.create_all()

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

    kasia = Writing(title='Kasia', text='A start-up starter, \n Plant based and is flourishing, \n Always smiling too', author=lily
     )
    cliff = Writing(title='Cliff', text='From a tiny land,\n He can watch sport all day long,\n The next crypto king?', author=lily)
    daniela = Writing(title='Daniela', text='Always lovely and warm,\n She asks all the best questions,\n And with that commute!', author=lily)
    dave = Writing(title='Dave', text='Blimey! hold my beer,\n It is not yet Christmas but,\n He is chuffed to bits', author=lily)
    gae = Writing(title='Gae', text='AirBnB boss,\n Novelist extraordinaire,\n LinkedIn King no more', author=lily)
    sheema = Writing(title='Sheema', text='She is a style queen,\n style as in Sass- but clothes too!\n Contest? She will win!', author=lily)
    ola = Writing(title='Ola', text='She\'s beautifully dressed,\n Finally has her own flat, \n She\'s earned it and more', author=lily)
    amy = Writing(title='Amy', text='From Bundy with love,\n When she goes out she goes out,\n Drink margaritas', author=lily)
    tom = Writing(title='Tom', text='Master of Pacman,\n Not a lover of pickle,\n A twirl though, yas queen', author=lily)
    talha = Writing(title='Talha', text='A man of few words,\n But those he chooses amuse,\n Nutella with what?!', author=lily)
    mia = Writing(title='Mia', text='Knows everyone,\n And what she wants too,\n Our linkedIn Queen', author=lily)
    charlie = Writing(title='Charlie', text='Is there a reason,\n That he eats so many nuts?\n Maybe for the "jokes"', author=lily)

    sim = Writing(title='Sim', text='Arms up in the air,\n Easy to tease but loved lots,\n Japanese Canteen?', author=lily)

    shane = Writing(title='Shane', text='Doesn\'t need google,\n Makes tetris look straightforward,\n Knows how to relax', author=lily)

    jack = Writing(title='Jack', text='He haz Cheeseburger,\n Dreams of leaving for MindGeek,\n Please wait \'til we\'re gone!', author=lily)

    wes = Writing(title='Wes', text='When it is deserved-\n Sassy as Sass! but really,\n So kind with his gifs', author=lily)


    edited_shane = Edit(title='Shane-Ed', original=shane,
    text='He is a very compotent coder who rarely uses Google and watches Netflix at the weekend',
    editor=laila)

    edited_jack = Edit(title='Jack-Ed', original=jack,
     text='He owns a cat called Cheeseburger and quite frequently refers to a dream of working for MindGeek', editor=laila)

    edited_wes = Edit(title='Wes-Ed', original=wes, text='He is a very nice young man', editor=laila)

    # shane = Writing(final_draft=edited_shane)
    #
    # jack = Writing(final_draft=edited_jack)
    #
    # wes = Writing(final_draft=edited_wes)


    db.session.add(lily)

    db.session.add(amy)
    db.session.add(tom)
    db.session.add(talha)
    db.session.add(shane)
    db.session.add(amy)
    db.session.add(charlie)
    db.session.add(wes)
    db.session.add(jack)
    db.session.add(ola)
    db.session.add(kasia)
    db.session.add(sim)
    db.session.add(sheema)
    db.session.add(gae)
    db.session.add(dave)
    db.session.add(daniela)
    db.session.add(cliff)
    db.session.add(mia)
    db.session.add(edited_shane)
    db.session.add(edited_wes)
    db.session.add(edited_jack)

    db.session.commit()
