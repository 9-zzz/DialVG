function press_button(button)
	input = {}
	input[button] = true
	joypad.set(1, input)
end

c = 0

function wait(seconds)
  local start = os.time()
  repeat until os.time() > start + seconds
end

function file_exists(name)
  local f=io.open(name,"r")
  if f~=nil then io.close(f) return true else return false end
end

-- A function to read text files
function read_file (filename)
  input = io.open(filename, "r") -- Open this file with the read flag.
  if input ~= nil then
    io.input(input) -- Set the input that the io library will read from.
    input_content = io.read() -- Read the contents of the file.
    io.close(input) -- Close the file.

    return input_content
  end

  return nil
end

function write_file (filename, text)
    output = io.open(filename, "w")
    io.output(output)
    io.write(text)
    io.close(output)
end

-- Infinite loop to take control over frame advancing.
while true do
  --if read_file("button.txt") ==  then
  if file_exists("button.txt") then
    button = read_file('button.txt')
    press_button(button)
    os.remove('button.txt')
    --write_file ("button.txt", "")
  end
  emu.frameadvance() -- This essentially tells FCEUX to keep running.
end
