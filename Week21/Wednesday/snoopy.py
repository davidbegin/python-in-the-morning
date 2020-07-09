


def register_response(response):
    if _snoopy_request.settings.get('USE_BUILTIN_PROFILER'):
        sys.setprofile(None)

    snoopy_data = _snoopy_request.data
    snoopy_data['end_time'] = datetime.datetime.now()
    snoopy_data['total_request_time'] = \
        (snoopy_data['end_time'] - snoopy_data['start_time'])

    if _snoopy_request.settings.get('USE_CPROFILE'):
        _snoopy_request.profiler.disable()
        profiler_result = StringIO.StringIO()
        profiler_stats = pstats.Stats(
            _snoopy_request.profiler, stream=profiler_result).sort_stats('cumulative')
        profiler_stats.print_stats()

        result = profiler_result.getvalue()
        if not _snoopy_request.settings.get('CPROFILE_SHOW_ALL_FUNCTIONS'):
            result = clean_profiler_result(result)
        snoopy_data['profiler_result'] = result
    return snoopy_data
