type ThemeToggleProps = {
  darkMode: boolean;
  setDarkMode: React.Dispatch<React.SetStateAction<boolean>>;
};
function ThemeToggle({ darkMode, setDarkMode }: ThemeToggleProps) {
  function toggleTheme() {
    setDarkMode(!darkMode);
  }
  return (
    <div className="card-box">
      <h2>Theme Toggle</h2>
      <p>
        Current Theme: <strong>{darkMode ? "Dark Mode" : "Light Mode"}</strong>
      </p>
      <button onClick={toggleTheme}>
        Switch to {darkMode ? "Light" : "Dark"} Mode
      </button>
    </div>
  );
}
export default ThemeToggle;