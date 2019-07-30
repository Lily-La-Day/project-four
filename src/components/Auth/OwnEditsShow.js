import React from 'react'
import axios from 'axios'
import Auth from '../../lib/Auth'
import FinalShow from './FinalShow'


class OwnEditsShow extends React.Component {
  constructor() {
    super()

    this.state = {  num: 0, 'edit': null  , confirmation: false, data: {}, finals: null, edited: null }
    this.addOne = this.addOne.bind(this)
    this.minusOne = this.minusOne.bind(this)
    this.selectFinal = this.selectFinal.bind(this)
    this.confirmFinal = this.confirmFinal.bind(this)


  }

  componentDidMount() {
    this.getFinals()
  }

  getFinals() {
    axios.get('/api/finals')
      .then(res => this.setState({ finals: res.data }))
      .catch(err => console.log(err))
  }

  addOne() {
    let number = this.state.num
    number += 1
    this.setState({ num: number })
  }

  minusOne() {
    let number = this.state.num
    number -= 1
    this.setState({ num: number })
  }



  selectFinal(edito) {

    const editId = { id: edito.id }
    const data = { edit: editId  }

    this.setState({ final: data })
    this.setState({ 'edit': data })
    this.setState({ edited: edito })
  }

  confirmFinal() {
    this.setState({ confirmation: true })
    this.postFinal()
  }

  postFinal() {
    axios.post('/api/finals', this.state.final, {
      headers: { Authorization: `Bearer ${Auth.getToken()}`}
    })
      .catch((err) => console.log(err))
    axios.post(`/api/writings/${this.state.edited.original.id}`, {
      headers: { Authorization: `Bearer ${Auth.getToken()}`}
    })
      .catch((err) => console.log(err))

  }

  render() {

    if(!this.props) return null

    return (
      <main>
        <h3> Here are the edits that have been submitted so far...</h3>
        <h6 className="subtitle"> When you find one you like, click to make final and confirm it as the finished draft!</h6>
        {!this.state.confirmation && <div className="edit-snippet-section">
          {this.props.edits.map((edito, i) => (
            <div key={i}>
              {(this.state.num === i) &&
                <section className="own-edits">
                  <h4>{edito.title}</h4>
                  <h6>{edito.text}</h6>
                  <h6>Submitted by {edito.editor.username}</h6>
                  {edito.rating &&


                    <h2>{edito.rating} </h2>}
                  {!this.state.final &&
                    <button className="make-final"
                      onClick={() => this.selectFinal(edito)}>Make Final</button>}
                  {this.state.final &&
                      <button className="make-final"
                        onClick={() => this.confirmFinal(edito)}>Are you sure!? Once you confirm
                  it is confirmed!</button>}
                </section> }
            </div>
          ))}

          {this.state.num < this.props.edits.length &&
               <button className="next-edit" onClick={this.addOne}>Next Edit</button>}
          {this.state.num > 0 &&
              <button className="next-edit" onClick={this.minusOne}>Last Edit</button>}

        </div>}
        {this.state.confirmation && <FinalShow edit={this.state.final}/>}
      </main>

    )
  }
}

export default OwnEditsShow
