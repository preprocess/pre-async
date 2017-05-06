--DESCRIPTION--

Test async macro

--GIVEN--

async function read($path) {
    $content = await \Amp\File\get($path);
    return $content . " await";
}

$async = async function($path) {
    $content = await \Amp\File\get($path);
    return $content;
};

--EXPECT--

function read($path)
{
    return call_user_func(function ($context·0) {
        return \Amp\coroutine(function () use ($context·0) {
            extract($context·0);

            $content = yield \Amp\File\get($path);
            return $content . " await";
        });
    }, get_defined_vars());
}

$async = call_user_func(function ($outer·2) {
    return function ($path) use ($outer·2) {
        return \Amp\coroutine(
                call_user_func(function ($inner·2) use ($outer·2) {
                    return function () use ($outer·2, $inner·2) {
                        extract($outer·2);
                        extract($inner·2);
                        $content = yield \Amp\File\get($path);
                        return $content;
                    };
                }, get_defined_vars())
            );
    };
}, get_defined_vars());
