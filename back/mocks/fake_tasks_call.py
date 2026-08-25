example = {
    'pagination': {
        'total_results': 3,
        'total_pages': 2,
        'first': {
            'href': 'https://api.example.org/v3/apps/ccc25a0f-c8f4-4b39-9f1b-de9f328d0ee5/tasks?page=1&per_page=2'
        },
        'last': {
            'href': 'https://api.example.org/v3/apps/ccc25a0f-c8f4-4b39-9f1b-de9f328d0ee5/tasks?page=2&per_page=2'
        },
        'next': {
            'href': 'https://api.example.org/v3/apps/ccc25a0f-c8f4-4b39-9f1b-de9f328d0ee5/tasks?page=2&per_page=2'
        },
        'previous': None,
    },
    'resources': [
        {
            'guid': 'd5cc22ec-99a3-4e6a-af91-a44b4ab7b6fa',
            'sequence_id': 1,
            'name': 'hello',
            'state': 'SUCCEEDED',
            'memory_in_mb': 512,
            'disk_in_mb': 1024,
            'result': {'failure_reason': None},
            'droplet_guid': '740ebd2b-162b-469a-bd72-3edb96fabd9a',
            'created_at': '2016-05-04T17:00:41Z',
            'updated_at': '2016-05-04T17:00:42Z',
            'links': {
                'self': {
                    'href': 'https://api.example.org/v3/tasks/d5cc22ec-99a3-4e6a-af91-a44b4ab7b6fa'
                },
                'app': {
                    'href': 'https://api.example.org/v3/apps/ccc25a0f-c8f4-4b39-9f1b-de9f328d0ee5'
                },
                'droplet': {
                    'href': 'https://api.example.org/v3/droplets/740ebd2b-162b-469a-bd72-3edb96fabd9a'
                },
            },
        },
        {
            'guid': '63b4cd89-fd8b-4bf1-a311-7174fcc907d6',
            'sequence_id': 2,
            'name': 'migrate',
            'state': 'FAILED',
            'memory_in_mb': 512,
            'disk_in_mb': 1024,
            'result': {'failure_reason': 'Exited with status 1'},
            'droplet_guid': '740ebd2b-162b-469a-bd72-3edb96fabd9a',
            'created_at': '2016-05-04T17:00:41Z',
            'updated_at': '2016-05-04T17:00:42Z',
            'links': {
                'self': {
                    'href': 'https://api.example.org/v3/tasks/63b4cd89-fd8b-4bf1-a311-7174fcc907d6'
                },
                'app': {
                    'href': 'https://api.example.org/v3/apps/ccc25a0f-c8f4-4b39-9f1b-de9f328d0ee5'
                },
                'droplet': {
                    'href': 'https://api.example.org/v3/droplets/740ebd2b-162b-469a-bd72-3edb96fabd9a'
                },
            },
        },
    ],
}

tasks_by_pcf_name = {
    'actions-reminders': [],
    'staff-viewer': [
        {
            'guid': '63b4cd89-fd8b-4bf1-a311-7174fcc907d6',
            'sequence_id': 5,
            'name': 'stop',
            'state': 'SUCCEEDED',
            'memory_in_mb': 512,
            'disk_in_mb': 1024,
            'result': {'failure_reason': None},
            'droplet_guid': '740ebd2b-162b-469a-bd72-3edb96fabd9a',
            'created_at': '2025-05-04T17:00:41Z',
            'updated_at': '2025-05-04T17:00:42Z',
            'links': {
                'self': {
                    'href': 'https://api.example.org/v3/tasks/63b4cd89-fd8b-4bf1-a311-7174fcc907d6'
                },
                'app': {
                    'href': 'https://api.example.org/v3/apps/ccc25a0f-c8f4-4b39-9f1b-de9f328d0ee5'
                },
                'droplet': {
                    'href': 'https://api.example.org/v3/droplets/740ebd2b-162b-469a-bd72-3edb96fabd9a'
                },
            },
        },
    ],
    'viewpoint': [
        {
            'guid': 'd5cc22ec-99a3-4e6a-af91-a44b4ab7b6fa',
            'sequence_id': 1,
            'name': 'start',
            'state': 'FAILED',
            'memory_in_mb': 512,
            'disk_in_mb': 1024,
            'result': {'failure_reason': 'Has not finished staging'},
            'droplet_guid': '740ebd2b-162b-469a-bd72-3edb96fabd9a',
            'created_at': '2025-12-15T10:47:01Z',
            'updated_at': '2025-12-15T10:47:01Z',
            'links': {
                'self': {
                    'href': 'https://api.example.org/v3/tasks/d5cc22ec-99a3-4e6a-af91-a44b4ab7b6fa'
                },
                'app': {
                    'href': 'https://api.example.org/v3/apps/ccc25a0f-c8f4-4b39-9f1b-de9f328d0ee5'
                },
                'droplet': {
                    'href': 'https://api.example.org/v3/droplets/740ebd2b-162b-469a-bd72-3edb96fabd9a'
                },
            },
        },
        {
            'guid': 'd5cc22ec-99a3-4e6a-af91-a44b4ab7b6fa',
            'sequence_id': 2,
            'name': 'restage',
            'state': 'FAILED',
            'memory_in_mb': 512,
            'disk_in_mb': 1024,
            'result': {'failure_reason': 'Exited with status 1'},
            'droplet_guid': '740ebd2b-162b-469a-bd72-3edb96fabd9a',
            'created_at': '2025-12-15T10:44:01Z',
            'updated_at': '2025-12-15T10:44:01Z',
            'links': {
                'self': {
                    'href': 'https://api.example.org/v3/tasks/d5cc22ec-99a3-4e6a-af91-a44b4ab7b6fa'
                },
                'app': {
                    'href': 'https://api.example.org/v3/apps/ccc25a0f-c8f4-4b39-9f1b-de9f328d0ee5'
                },
                'droplet': {
                    'href': 'https://api.example.org/v3/droplets/740ebd2b-162b-469a-bd72-3edb96fabd9a'
                },
            },
        },
        {
            'guid': '63b4cd89-fd8b-4bf1-a311-7174fcc907d6',
            'sequence_id': 3,
            'name': 'start',
            'state': 'FAILED',
            'memory_in_mb': 512,
            'disk_in_mb': 1024,
            'result': {'failure_reason': 'Exited with status 1'},
            'droplet_guid': '740ebd2b-162b-469a-bd72-3edb96fabd9a',
            'created_at': '2025-12-15T10:40:01Z',
            'updated_at': '2025-12-15T10:40:01Z',
            'links': {
                'self': {
                    'href': 'https://api.example.org/v3/tasks/63b4cd89-fd8b-4bf1-a311-7174fcc907d6'
                },
                'app': {
                    'href': 'https://api.example.org/v3/apps/ccc25a0f-c8f4-4b39-9f1b-de9f328d0ee5'
                },
                'droplet': {
                    'href': 'https://api.example.org/v3/droplets/740ebd2b-162b-469a-bd72-3edb96fabd9a'
                },
            },
        },
        {
            'guid': '63b4cd89-fd8b-4bf1-a311-7174fcc907d6',
            'sequence_id': 4,
            'name': 'upload bits',
            'state': 'SUCCEEDED',
            'memory_in_mb': 512,
            'disk_in_mb': 1024,
            'result': {'failure_reason': None},
            'droplet_guid': '740ebd2b-162b-469a-bd72-3edb96fabd9a',
            'created_at': '2025-12-15T10:30:01Z',
            'updated_at': '2025-12-15T10:30:01Z',
            'links': {
                'self': {
                    'href': 'https://api.example.org/v3/tasks/63b4cd89-fd8b-4bf1-a311-7174fcc907d6'
                },
                'app': {
                    'href': 'https://api.example.org/v3/apps/ccc25a0f-c8f4-4b39-9f1b-de9f328d0ee5'
                },
                'droplet': {
                    'href': 'https://api.example.org/v3/droplets/740ebd2b-162b-469a-bd72-3edb96fabd9a'
                },
            },
        },
        {
            'guid': '63b4cd89-fd8b-4bf1-a311-7174fcc907d6',
            'sequence_id': 5,
            'name': 'stop',
            'state': 'SUCCEEDED',
            'memory_in_mb': 512,
            'disk_in_mb': 1024,
            'result': {'failure_reason': None},
            'droplet_guid': '740ebd2b-162b-469a-bd72-3edb96fabd9a',
            'created_at': '2025-12-15T10:28:01Z',
            'updated_at': '2025-12-15T10:28:01Z',
            'links': {
                'self': {
                    'href': 'https://api.example.org/v3/tasks/63b4cd89-fd8b-4bf1-a311-7174fcc907d6'
                },
                'app': {
                    'href': 'https://api.example.org/v3/apps/ccc25a0f-c8f4-4b39-9f1b-de9f328d0ee5'
                },
                'droplet': {
                    'href': 'https://api.example.org/v3/droplets/740ebd2b-162b-469a-bd72-3edb96fabd9a'
                },
            },
        },
    ],
    'performance-management': [],
    'reporting-hub': [],
    'pi-services-viewpoint': [],
    'pi-services-performance-management': [],
    'pi-services-reporting-hub': [],
    'cost-allocations': [],
    'cost-insights': [
        {
            'guid': '63b4cd89-fd8b-4bf1-a311-7174fcc907d6',
            'sequence_id': 3,
            'name': 'start',
            'state': 'SUCCEEDED',
            'memory_in_mb': 512,
            'disk_in_mb': 1024,
            'result': {'failure_reason': None},
            'droplet_guid': '740ebd2b-162b-469a-bd72-3edb96fabd9a',
            'created_at': '2025-12-15T10:35:41Z',
            'updated_at': '2025-12-15T10:35:42Z',
            'links': {
                'self': {
                    'href': 'https://api.example.org/v3/tasks/63b4cd89-fd8b-4bf1-a311-7174fcc907d6'
                },
                'app': {
                    'href': 'https://api.example.org/v3/apps/ccc25a0f-c8f4-4b39-9f1b-de9f328d0ee5'
                },
                'droplet': {
                    'href': 'https://api.example.org/v3/droplets/740ebd2b-162b-469a-bd72-3edb96fabd9a'
                },
            },
        },
        {
            'guid': '63b4cd89-fd8b-4bf1-a311-7174fcc907d6',
            'sequence_id': 4,
            'name': 'upload bits',
            'state': 'SUCCEEDED',
            'memory_in_mb': 512,
            'disk_in_mb': 1024,
            'result': {'failure_reason': None},
            'droplet_guid': '740ebd2b-162b-469a-bd72-3edb96fabd9a',
            'created_at': '2025-12-15T10:33:41Z',
            'updated_at': '2025-12-15T10:33:42Z',
            'links': {
                'self': {
                    'href': 'https://api.example.org/v3/tasks/63b4cd89-fd8b-4bf1-a311-7174fcc907d6'
                },
                'app': {
                    'href': 'https://api.example.org/v3/apps/ccc25a0f-c8f4-4b39-9f1b-de9f328d0ee5'
                },
                'droplet': {
                    'href': 'https://api.example.org/v3/droplets/740ebd2b-162b-469a-bd72-3edb96fabd9a'
                },
            },
        },
        {
            'guid': '63b4cd89-fd8b-4bf1-a311-7174fcc907d6',
            'sequence_id': 5,
            'name': 'stop',
            'state': 'SUCCEEDED',
            'memory_in_mb': 512,
            'disk_in_mb': 1024,
            'result': {'failure_reason': None},
            'droplet_guid': '740ebd2b-162b-469a-bd72-3edb96fabd9a',
            'created_at': '2025-12-15T10:29:41Z',
            'updated_at': '2025-12-15T10:29:42Z',
            'links': {
                'self': {
                    'href': 'https://api.example.org/v3/tasks/63b4cd89-fd8b-4bf1-a311-7174fcc907d6'
                },
                'app': {
                    'href': 'https://api.example.org/v3/apps/ccc25a0f-c8f4-4b39-9f1b-de9f328d0ee5'
                },
                'droplet': {
                    'href': 'https://api.example.org/v3/droplets/740ebd2b-162b-469a-bd72-3edb96fabd9a'
                },
            },
        },
    ],
    'pi-services-cost-allocations': [],
    'pi-services-cost-insights': [
        {
            'guid': '63b4cd89-fd8b-4bf1-a311-7174fcc907d6',
            'sequence_id': 5,
            'name': 'stop',
            'state': 'SUCCEEDED',
            'memory_in_mb': 512,
            'disk_in_mb': 1024,
            'result': {'failure_reason': None},
            'droplet_guid': '740ebd2b-162b-469a-bd72-3edb96fabd9a',
            'created_at': '2025-12-15T10:30:41Z',
            'updated_at': '2025-12-15T10:30:42Z',
            'links': {
                'self': {
                    'href': 'https://api.example.org/v3/tasks/63b4cd89-fd8b-4bf1-a311-7174fcc907d6'
                },
                'app': {
                    'href': 'https://api.example.org/v3/apps/ccc25a0f-c8f4-4b39-9f1b-de9f328d0ee5'
                },
                'droplet': {
                    'href': 'https://api.example.org/v3/droplets/740ebd2b-162b-469a-bd72-3edb96fabd9a'
                },
            },
        },
    ],
    'aiden': [],
    'pi-services-aiden': [],
    'pi-services-aiden-rag': [],
    'whatif-core': [],
    'whatif-core-backend': [],
    'starfleet-archives': [],
    'pi-services-starfleet-archives': [],
}
