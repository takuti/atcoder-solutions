s = gets.chomp.to_s
t = gets.chomp.to_s
u = ['a', 't', 'c', 'o', 'd', 'e', 'r']
check = true
for i in 0...s.size
  next if s[i]==t[i]
  if s[i]=='@' && u.include?(t[i])
    next
  elsif t[i]=='@' && u.include?(s[i])
    next
  end
  check=false
  break
end

if check
  puts 'You can win'
else
  puts 'You will lose'
end
