import React from 'react'
import axios from 'axios'
import Auth from '../../lib/Auth'
import { Link } from 'react-router-dom'






class EditRate extends React.Component {
  constructor() {
    super()

    this.state = {  'rating': {}, hasRated: false, editor: null   }
    this.starNumber =  0
    this.finalStarNumber= 0
    this.rated = false
    this.currentEdit= 1
    this.starRating = this.starRating.bind(this)
    this.rate = this.rate.bind(this)
    this.ratingCheck = this.ratingCheck.bind(this)
  }

  starRating(e) {
    const one = document.querySelector('.one')
    const two = document.querySelector('.two')
    const three = document.querySelector('.three')
    const four = document.querySelector('.four')
    const five = document.querySelector('.five')

    if(!this.rated)
      if(e.target.classList.contains('one')){
        one.classList.toggle('starAfter')
        this.setState({ rating: 1 })
      }  else if(e.target.classList.contains('two')){
        one.classList.toggle('starAfter')
        two.classList.toggle('starAfter')
        this.setState({ rating: 2 })
      }  else if(e.target.classList.contains('three')){
        one.classList.toggle('starAfter')
        two.classList.toggle('starAfter')
        three.classList.toggle('starAfter')
        this.setState({ rating: 3 })
      }  else if(e.target.classList.contains('four')){
        one.classList.toggle('starAfter')
        two.classList.toggle('starAfter')
        three.classList.toggle('starAfter')
        four.classList.toggle('starAfter')
        this.setState({ rating: 4 })
      } else if(e.target.classList.contains('five')){
        one.classList.toggle('starAfter')
        two.classList.toggle('starAfter')
        three.classList.toggle('starAfter')
        four.classList.toggle('starAfter')
        five.classList.toggle('starAfter')
        this.setState({ rating: 5 })
      }
    document.querySelector('p').classList.remove('none')
  }

  rate() {

    console.log(this.state.rating)
    console.log('rating')
    axios.post(`/api/edits/${this.props.edit.id}/like`, this.state,  {
      headers: { Authorization: `Bearer ${Auth.getToken()}`}
    })
      .catch((err) => console.log(err))
    this.rated = true
    document.querySelector('.thank-you').style.display = 'block'
    document.querySelector('.rateButton').style.display = 'none'
  }


  getData(){
    axios.get('/api/editor', {
      headers: { Authorization: ` ${Auth.getToken()}` }
    })
      .then(res => this.setState({ editor: res.data }))
      .then(()=> this.ratingCheck())
      .catch(() => this.setState({ error: 'Invalid Crendentials' }))
  }

  componentDidMount() {
    this.getData()
  }

  ratingCheck() {
    if(this.props.edit.liked_by.map(like => like.id).includes(this.state.editor.id))
      this.setState({ hasRated: true })
  }




  render() {
    if (!this.props.edit) return null
    if (!this.props.edit) return null
    if (!this.state.editor) return null

    return (
      <main>
        <h2  className="writing-title">{this.props.edit.title}</h2>
        <div className="snippet">
          <h5 className="edit-snippet"> {this.props.edit.text}</h5>
        </div>
        {!this.state.hasRated &&  <div>
          <div className="content">
            <h3>Rate This Edit</h3>
            <div className="wrapper snippet">
              <img src="/assets/star.svg" className="starBefore one"  onClick={this.starRating}/>
              <img src="/assets/star.svg"  className="starBefore two" onClick={this.starRating}/>
              <img src="/assets/star.svg"  className="starBefore three" onClick={this.starRating}/>
              <img src="/assets/star.svg" className="starBefore four" onClick={this.starRating}/>
              <img src="/assets/star.svg" className="starBefore five" onClick={this.starRating}/>
            </div>
          </div>
          <div className="rating-container snippet">
            <p className='none star-text'> Click below to confirm your rating </p>
            <button className="rateButton button" onClick={this.rate} > rate </button>
            <h3 className="thank-you"> Thank you for rating! This edit currently has a rating of {this.props.edit.rating + this.state.rating}</h3>
          </div>
        </div>}

        {this.state.hasRated && <h6 className="snippet"> You have already rated this one! It currently has a rating of {this.props.edit.rating}</h6>}
        <Link to={`/edit-writings/${this.props.edit.original.id}/edit`}> <button className="sub edit-button"> Submit an edit! </button></Link>
      </main>


    )
  }
}

export default EditRate



// import React from 'react'
// import EditRate from './EditRate'
//
// class EditsShow extends React.Component {
//   constructor() {
//     super()
//     this.state = { edits: [] , num: 0 }
//     this.addOne = this.addOne.bind(this)
//     this.minusOne = this.minusOne.bind(this)
//   }
//
//   addOne() {
//     let number = this.state.num
//     number += 1
//     this.setState({ num: number })
//   }
//   minusOne() {
//     let number = this.state.num
//     number -= 1
//     this.setState({ num: number })
//   }
//   render() {
//
//     if (!this.props.edits) return null
//     if(!this.props)
//
//       return (
//         <main>
//           <div className="edit-snippet-section">
//             {this.props.edits.map((edit, i) => (
//               <div key={i}>
//                 { (this.state.num === i) &&
//               <EditRate edit={edit} writing={this.props.writing}/> }
//               </div>
//             ))}
//             {this.state.num < this.props.edits.length && <button onClick={this.addOne} className="show-button">Next edit</button>}
//             {this.state.num > 0 && <button onClick={this.minusOne}  className="show-button">Last edit</button>}
//           </div>
//         </main>
//
//       )
//   }
// }
//
// export default EditsShow
