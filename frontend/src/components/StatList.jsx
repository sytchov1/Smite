import React from 'react'
import Stat from './Stat'

function StatList(props) {
  return (
    <div className='StatList'>
        {props.stats.map((stat, index) =>
            <Stat key={index} stat={stat}></Stat>
        )}
    </div>
  )
}

export default StatList