from django.http import JsonResponse
from django.db import connection

def get_db_health(request):
    try:
        with connection.cursor() as cursor:
            # Fetch Active Connections
            cursor.execute("SHOW GLOBAL STATUS LIKE 'Threads_connected';")
            active_connections = cursor.fetchone()[1]

            # Fetch Total Queries Processed
            cursor.execute("SHOW GLOBAL STATUS LIKE 'Queries';")
            total_queries = cursor.fetchone()[1]

            # Fetch Uptime
            cursor.execute("SHOW GLOBAL STATUS LIKE 'Uptime';")
            uptime = cursor.fetchone()[1]

            # Fetch Maximum Allowed Connections
            cursor.execute("SHOW GLOBAL VARIABLES LIKE 'max_connections';")
            max_connections = cursor.fetchone()[1]

            # Fetch Threads Running
            cursor.execute("SHOW GLOBAL STATUS LIKE 'Threads_running';")
            threads_running = cursor.fetchone()[1]

            # Fetch Slow Queries Count
            cursor.execute("SHOW GLOBAL STATUS LIKE 'Slow_queries';")
            slow_queries = cursor.fetchone()[1]

            # Fetch Query Cache Hit Rate
            cursor.execute("SHOW GLOBAL STATUS LIKE 'Qcache_hits';")
            qcache_hits = cursor.fetchone()[1]

            cursor.execute("SHOW GLOBAL STATUS LIKE 'Qcache_inserts';")
            qcache_inserts = cursor.fetchone()[1]

            query_cache_hit_rate = int(qcache_hits) / (int(qcache_hits) + int(qcache_inserts) + 1) * 100 if int(qcache_hits) > 0 else 0

            # Fetch Buffer Pool Usage
            cursor.execute("SHOW GLOBAL STATUS LIKE 'Innodb_buffer_pool_pages_free';")
            buffer_pool_free = cursor.fetchone()[1]

            cursor.execute("SHOW GLOBAL STATUS LIKE 'Innodb_buffer_pool_pages_total';")
            buffer_pool_total = cursor.fetchone()[1]

            buffer_pool_usage = (1 - int(buffer_pool_free) / int(buffer_pool_total)) * 100 if int(buffer_pool_total) > 0 else 0

        return JsonResponse({
            "active_connections": active_connections,
            "max_connections": max_connections,
            "total_queries": total_queries,
            "uptime_seconds": uptime,
            "threads_running": threads_running,
            "slow_queries": slow_queries,
            "query_cache_hit_rate": f"{query_cache_hit_rate:.2f}%",
            "buffer_pool_usage": f"{buffer_pool_usage:.2f}%"
        })

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
