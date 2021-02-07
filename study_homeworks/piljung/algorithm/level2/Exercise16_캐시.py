# 15. 캐시 (2018 kakao blind recruitment)

def solution(cacheSize, cities):
    time = 0
    cache = []

    cities = [city.lower() for city in cities]

    if cacheSize != 0:  # cash 크기가 0인 경우 for문을 돌지 않도록 하여 효율성 up
        for city in cities:
            # print(city)
            # print(cache)
            # print(time)
            if city in cache:  # cash hit (캐시안에 현재 값이 있는 경우)
                cache.pop(cache.index(city))
                cache.append(city)
                time += 1
            else:  # cash miss(캐시 안에 현재 값이 없는 경우)
                if len(cache) < cacheSize:
                    cache.append(city)
                    time += 5

                else:
                    cache.pop(0)  # 가장 먼저 들어온 캐시 지우고 동일한 cashmiss 액션
                    cache.append(city)
                    time += 5

    else:
        time += len(cities) * 5

    return time
