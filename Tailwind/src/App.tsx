import { useEffect, useState } from "react";
function App() {
  const [task, setTask] = useState<string>("");
  const [tasks, setTasks] = useState<string[]>([]);
  useEffect(() => {
    console.log("App mounted");
  }, []);
  function handleSubmit(e: React.FormEvent<HTMLFormElement>) {
    e.preventDefault();
    if (task.trim() === "") return;
    setTasks([...tasks, task]);
    setTask("");
  }
  return (
    <div className="min-h-screen bg-gray-100 flex justify-center w-full">
      <div className="bg-white shadow-lg rounded-xl p-6 w-full">
        <h1 className="text-2xl font-bold text-center text-blue-700 mb-5">
          Task List
        </h1>

        <form onSubmit={handleSubmit} className="flex gap-2 mb-5">
          <input
            type="text"
            placeholder="Enter a task"
            value={task}
            onChange={(e) => setTask(e.target.value)}
            className="flex-1 border border-gray-300 px-3 py-2 rounded-lg"
          />
          <button
            type="submit"
            className="bg-blue-600 text-white px-4 py-2 rounded-lg"
          >
            Add
          </button>
        </form>

        <ul className="space-y-2">
          {tasks.map((item, index) => (
            <li
              key={index}
              className="bg-gray-100 p-3 rounded-lg border border-gray-200"
            >
              {item}
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}
export default App;