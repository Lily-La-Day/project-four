import React from 'react'
import axios from 'axios'
import Auth from '../../lib/Auth'

const Diff = require('diff')




class EditCreate extends React.Component {
  constructor() {
    super()

    this.state = { writing: null, data: { }, text: [], word: '' }
    this.handleChange = this.handleChange.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
    this.makeArray = this.makeArray.bind(this)
    this.setWord = this.setWord.bind(this)


  }

  handleChange({ target: { name, value }}) {

    const data = {...this.state.data, [name]: value, original: { id: this.state.writing.id } }

    this.setState({ data, error: ''})


  }

  print() {
    console.log('working')
  }



  makeArray() {

    const text = [this.state.writing.text.split(' ')][0]

    text.map((word) => {
      const span = document.createElement('span')

      span.textContent = `${word} `
      word = span






    })

    this.setState({ text: text })

    // console.log()
    // console.log(event.target.selectionStart)

  }

  getWords() {
    axios.get(`https://wordsapiv1.p.mashape.com/words/${this.state.word}`,  {
      headers: { 'X-Mashape-Key': '3460369150msh8609f9e537602d4p1446a9jsnb662278c8800'}
    })
      .then((res) => {
        console.log(res.data)
      })

  }


  handleSubmit(e) {
    e.preventDefault()
    console.log(this.state.data)
    axios.post('/api/edits', this.state.data,  {
      headers: { Authorization: `Bearer ${Auth.getToken()}`}
    })

      .then(() => {

        this.props.history.push('/writings')
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

  diff(oldStr, newStr){
    console.log(Diff.diffChars(oldStr, newStr))
  }
  log(e) {
    console.log(e.target.value.innerText)
  }

  render() {
    if (!this.state.writing) return null

    {this.state.word && this.getWords()}

    // this.diff('human', 'humat')
    const { writing } =  this.state

    return (

      <main >
        <div className="edit-container" onMouseOver={this.makeArray}>
          <div className ="original">
            <div>
              <h2 className="original-title">{writing.title}</h2>

              <div className="writings-container scroll" >
                {this.state.text.map((word, i) => <p key={i} onClick={this.setWord} className="words">{word}</p>)}

              </div>

            </div>

          </div>


          <form className="form-style create-edit" onSubmit={this.handleSubmit}  >

            <h3>Submit an Edit</h3>

            <label className='label'>Title</label>
            <div className="control">
              <input
                onChange = {this.handleChange}
                className="input"
                name="title"

                defaultValue={this.state.writing.title}/>
            </div>
            <label className='label'>Your Edit</label>
            <div className="control">
              <textarea
                onChange = {this.handleChange}
                type="text"
                className="submit-writing input"
                name="text"

                defaultValue= {this.state.writing.text}



              />
            </div>


            <button type="submit" className="button" > Submit your edit. </button>


          </form>
        </div>
      </main>

    )
  }
}

export default EditCreate
