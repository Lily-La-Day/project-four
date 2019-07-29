import React from 'react'
import axios from 'axios'
import Auth from '../../lib/Auth'
import FinalShow from './FinalShow'

// import { Link } from 'react-router-dom'






class OwnEditsShow extends React.Component {
  constructor() {
    super()

    this.state = {  num: 0, 'edit': null  , confirmation: false, data: {}, finals: null }
    this.addOne = this.addOne.bind(this)
    this.minusOne = this.minusOne.bind(this)
    this.selectFinal = this.selectFinal.bind(this)
    this.confirmFinal = this.confirmFinal.bind(this)


  }

  // componentDidMount() {
  //   this.getFinals()
  // }
  //
  // getFinals() {
  //   axios.get('/api/finals')
  //     .then(res => this.setState({ finals: res.data }))
  //     .catch(err => console.log(err))
  // }
  //
  // filterFinals() {
  //
  //
  //   console.log(this.props.edits.forEach(edit => this.state.finals.filter(final =>
  //     console.log(final.edit.id, edit.id)
  //     (final.edit.id !== edit.id)
  //
  //   )))
  //
  // }



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
  //
  // selectFinal(edit) {
  //
  //   this.setState({ edit_id: edit.id })
  //   this.setState({ final: edit })
  //   console.log(edit.id)
  //   console.log(edit)
  //
  // }

  selectFinal(edito) {

    const edit_id = { id: edito.id }

    const data = { edit: edit_id  }

    this.setState({ final : data })
    this.setState({ 'edit': data })
  }



  confirmFinal() {

    this.setState({ confirmation: true })
    this.postFinal()
  }



  postFinal() {
    console.log(this.state.final)
    axios.post('/api/finals', this.state.final, {
      headers: { Authorization: `Bearer ${Auth.getToken()}`}


    })
      .catch((err) => console.log(err))

  }


  render() {
console.log(this.props, this.state)
    if (!this.props.edits) return null
    if(!this.props)
    console.log('final', this.state.final)
    return (
      <main>
        {!this.state.confirmation && <div className="edit-snippet-section">
          {this.props.edits.map((edito, i) => (
            <div key={i}>
              {(this.state.num === i) &&
                <section className="own-edits">
                  <h4>{edito.title}</h4>
                  <h6>{edito.text}</h6>
                  {edito.rating &&
                    <h2>{edito.rating} </h2>}
                    {!this.state.final && <button className="make-final" onClick={() => this.selectFinal(edito)}>Make Final</button>}
                  </section> }


              {this.state.final && <button className="make-final" onClick={() => this.confirmFinal(edito)}>Are you sure!? Once you confirm
            it is confirmed!</button>}

            </div>

          ))}

        {this.state.num < this.props.edits.length &&  <button className="next-edit" onClick={this.addOne}>Next Edit</button>}
        {this.state.num > 0 && <button className="next-edit" onClick={this.minusOne}>Last Edit</button>}

        </div>}
        {this.state.confirmation && <FinalShow edit={this.state.final}/>}

  </main>

    )
  }
}

export default OwnEditsShow
