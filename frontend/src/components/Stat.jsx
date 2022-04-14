import React from 'react'

function Stat(props) {
  return (
    <div className='Stat'>
        <div className='Stat-name'>{props.stat['name']}</div>
        <div className='Stat-value'>{props.stat['value']}</div>
    </div>
  )
}

export default Stat