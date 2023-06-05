const Button = ({children, onClick}) => {

    return (
        <button onClick={onClick} className="bg-[#FA0] w-32 h-10 rounded-2xl font-sans font-bold">{children}</button>
    );
}
 
export default Button;