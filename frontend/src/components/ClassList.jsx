import React from 'react'
import ClassItem from './ClassItem'

function ClassList(props) {
  return (
    <div className='ClassList'>
      {props.cls.map((cl, index) =>
        <ClassItem key={index} cl={cl}/>
      )}
    </div>
  )
}

export default ClassList