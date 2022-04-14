import React from 'react'
import Select from 'react-select'

function CustomSelect(props) {
  return (
    <Select
      options={props.options}
      value={props.options.find(opt => opt.value === props.value)}
      onChange={props.onChange}
      theme={(theme) => ({
        ...theme,
        borderRadius: 0,
        colors: {
          ...theme.colors,
          primary25: '#151506',
          primary: 'goldenrod'
        },
      })}
      styles={{
        control: (base) => ({
          ...base,
          backgroundColor: '#353535',
          border: 'none',
          borderBottom: '1px solid gray',
          ':hover': {
            ...base[':hover'],
            borderColor: 'gray',
          },
        }),
        option: (base) => ({
          ...base,
          color: 'white',
          ':active': {
            ...base[':active'],
            backgroundColor: '#F7D377',
          },
        }),
        menuList: (base) => ({
          ...base,
          backgroundColor: '#353535',
          border: '1px solid #F7D377',
        }),
        singleValue: (base) => ({
          ...base,
          color: 'white',
        }),
        indicatorsContainer: (base) => ({
          ...base,
          cursor: 'pointer',
        }),
        dropdownIndicator: (base) => ({
          ...base,
          color: '#F7D377',
          '&:hover':{
            color:'#F7D377',
          },
        })
      }}
      components={{
        IndicatorSeparator: () => null,
        Input: () => null,
      }}
    />
  )
}

export default CustomSelect