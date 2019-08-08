import React from 'react'
import axios from 'axios'
import Auth from '../../lib/Auth'
class EditCreate extends React.Component {
  constructor() {
    super()

    this.state = {
      writing: null,
      data: { },
      autoWordData: [],
      text: [],
      word: '',
      wordData: [],
      textTwo: '',
      query: '',
      highlighted: '',
      synonyms: null,
      autosynonyms: null,
      definition: false }

    this.handleChange = this.handleChange.bind(this)
    this.changeMode = this.changeMode.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
    this.makeArray = this.makeArray.bind(this)
    this.setWord = this.setWord.bind(this)
    this.handleInputChange = this.handleInputChange.bind(this)
    this.matchWord = this.matchWord.bind(this)
    this.autoGetWords = this.autoGetWords.bind(this)
  }

  handleInputChange(e) {
    e.preventDefault()
    this.setState({
      query: this.search.value
    })
  }

  handleChange({ target: { name, value }}) {
    let text = []
    const data = {...this.state.data, [name]: value, original: { id: this.state.writing.id } }
    this.setState({ data, error: ''})
    text = data.text.split('.').join('')
    text = text.split(' ')
    this.setState({ textTwo: text })
    this.setState({
      query: text[text.length - 2]
    })
  }

  changeMode() {
    if(!this.state.definition)
      this.setState({ definition: true })
    else if(this.state.definition)
      this.setState({ definition: false })

  }


  matchWord(e) {
    if(this.state.textTwo.length > 3) {
      if(e.keyCode === 32){
        this.state.textTwo.forEach((word) => {
          if(word.length > 1 && word === this.state.query) {
            console.log('word')

          }
        })
        this.setState({
          query: ''
        })

      }
    }

  }


  makeArray() {
    const text = [this.state.writing.text.split(' ')][0]
    text.map((word) => {
      word = word.split('.').join('')
      word = word.split(' ')
      const span = document.createElement('span')
      span.textContent = `${word} `
      word = span
    })
    this.setState({ text: text })
  }

  getWords() {
    axios.get(`https://wordsapiv1.p.mashape.com/words/${this.state.word}`,  {
      headers: { 'X-Mashape-Key': '3460369150msh8609f9e537602d4p1446a9jsnb662278c8800' }
    })
      .then((res) => {
        this.setState({wordData: res.data.results})
        let synonyms = []
        synonyms =  res.data.results.map(result => result.synonyms)
        synonyms = synonyms.filter(array => array)
        this.setState({ synonyms: synonyms })

      })
      .then(this.setState({wordData: ''}))


  }

  autoGetWords(e) {

    if(e.keyCode === 32){
      axios.get(`https://wordsapiv1.p.mashape.com/words/${this.state.query}`,  {
        headers: { 'X-Mashape-Key': '3460369150msh8609f9e537602d4p1446a9jsnb662278c8800' }
      })
        .then((res) => {
          this.setState({autoWordData: res.data.results})
          let synonyms = []
          synonyms =  res.data.results.map(result => result.synonyms)
          synonyms = synonyms.filter(array => array)
          this.setState({ autosynonyms: synonyms })
        })

    }

    this.setState({ synonyms: null })
  }

  handleSubmit(e) {
    e.preventDefault()
    axios.post('/api/edits', this.state.data,  {
      headers: { Authorization: `Bearer ${Auth.getToken()}`}
    })
      .then(() => {
        this.props.history.push('/edit-writings')
      })
      .catch((err) => console.log(err))
  }

  setWord(e) {
    this.setState({word: e.target.innerText})
  }


  componentDidMount() {

    axios.get(`/api/writings/${this.props.match.params.id}`)
      .then(res => this.setState({ writing: res.data, original: { id: res.data.id } }))
      .catch(err => console.log(err))
  }


  render() {
    if (!this.state.writing) return null
    const { writing } =  this.state
    console.log('deployed')
    console.log(this.state.query)
    return (
      <main >
        <div className="edit-container"
          onMouseOver={this.makeArray}>
          <div onClick={this.stateCheck}
            className ="original">
            <div>
              <h3 className="original-title">{writing.title}</h3>

              {!this.state.definition &&
                <button className="mode" onClick={this.changeMode}>Dictionary Mode</button>}
              {this.state.definition &&
                <button className="mode" onClick={this.changeMode}>Thesaurus Mode</button>}

              <div className="writings-container scroll" >
                {!this.state.textTwo &&
                  this.state.text.map((word) => <p key={word.id} onMouseDown={this.setWord} onMouseUp={()=>this.getWords()} className="words highlighted">{word}</p>)}
                {this.state.textTwo &&
                  this.state.textTwo.map((word) => <p key={word.id} onMouseDown={this.setWord} onMouseUp={()=>this.getWords()} className={word} >{word}</p>)}
              </div>
              {this.state.definition &&
                 <div className="alts container" >
                   {this.state.word &&
                  this.state.wordData &&
                   this.state.wordData.map((word, i) =>
                     (i < 20) &&
                   <p className="alt-word" key={word.id}>{word.definition}</p>)}
                   {this.state.autoWordData &&
                      this.state.autoWordData.map((word, i) =>
                        (i < 20) &&
                   <p className="alt-word" key={word.id}>{word.definition}</p>)}

                 </div>}
              {!this.state.definition &&
                 <div className="alts container" >
                   {this.state.synonyms &&
                  this.state.synonyms.map((word, i) =>
                    (i < 20) &&
                  word.map(el => <p className="alt-word" key={el.id}>{el}</p>)
                  )}
                   {!this.state.synonyms &&
                    this.state.autosynonyms && this.state.autosynonyms.map((word, i) =>
                     (i < 20) &&
                  word.map(el => <p className="alt-word" key={el.id}>{el}</p>)
                   )}
                 </div>}
            </div>
          </div>
          <form className="form-style create-edit" onSubmit={this.handleSubmit}  >
            <div className="control">
              <input
                onChange = {this.handleChange}
                className="edit-title input"
                name="title"
                defaultValue={this.state.writing.title}/>
            </div>
            <label className='form-small label'>The Original</label>
            <div className="control">
              <textarea readOnly
                type="text"
                id="original-writing"
                className="original-writing fixed submit-writing input"
                name="text"
                value= {this.state.writing.text}
              />
            </div>
            <label className='form-small label'>Your Edit</label>
            <div className="control">
              <textarea
                onChange = {this.handleChange}
                type="text"
                className="submit-writing input"
                name="text"
                defaultValue= {this.state.writing.text}
                onKeyDown={this.matchWord}
                onKeyUp={this.autoGetWords}
              />
            </div>
            <button type="submit" className="submit-button" > Submit your edit. </button>
          </form>
          <form className="search">
            <input
              placeholder="Search words..."
              ref={input => this.search = input}
              onChange={this.handleInputChange}
              onKeyUp={this.matchWord}
            />
            <button type="submit" className="searchButton">
              <i className="fa fa-search"></i>
            </button>
            <p className="highlighted">{this.state.query}</p>
          </form>
        </div>
      </main>

    )
  }
}

export default EditCreate
