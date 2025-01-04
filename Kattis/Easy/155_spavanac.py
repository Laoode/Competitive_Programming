h,m = map(int, input().split())

minute = 60
hour = 24
m_early = m-45
if m_early < 0:
    time_h = h-1
    m_early = abs(m_early)
    m_early = int(m_early)
    time_m = minute-m_early
    if time_h<0:
        time_h= hour+time_h
    print(time_h, time_m)
else:
    print(h, m_early)