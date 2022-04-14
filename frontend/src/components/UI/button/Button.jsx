import React from "react";
import classes from './Button.module.css';

const Button = ({children, className, ...props}) => {
    return (
        <button {...props} className={className + ' ' + classes.button}>
            {children}
        </button>
    );
};

export default Button;