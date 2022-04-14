import React from 'react'

function ClassItem(props) {
  return (
    <div className='ClassItem'>
        <div className='class-icon' style={{backgroundImage: `url(https://wow.zamimg.com/images/wow/icons/large/${props.cl.icon}.jpg)`}}></div>
    </div>
  )
}

export default ClassItem